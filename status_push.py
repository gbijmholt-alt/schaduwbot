#!/usr/bin/env python3
"""Stuurt de toestand van de server naar de GitHub-branch 'status' (bestand status.md).
Gebruikt alleen de Python-standaardbibliotheek, zodat het ook werkt als de installatie
van de bot zelf is mislukt. Geheimen worden altijd weggelakt: de repo is openbaar.

Gebruik: python3 status_push.py "<korte melding>"
Omgeving: GITHUB_REPO, GITHUB_TOKEN, HELIUS_API_KEY (alleen voor weglakken)."""
import base64, hashlib, json, os, re, socket, subprocess, sys, time, urllib.error, urllib.request

API = os.getenv("GITHUB_API", "https://api.github.com")
REPO = os.getenv("GITHUB_REPO", "")
TOKEN = os.getenv("GITHUB_TOKEN", "")
BRANCH = "status"
BOT_DIR = os.getenv("BOT_DIR", "/opt/schaduwbot")


def redact(text: str) -> str:
    for secret in (TOKEN, os.getenv("HELIUS_API_KEY", "")):
        if secret and len(secret) > 6:
            text = text.replace(secret, "***")
    text = re.sub(r"github_pat_[A-Za-z0-9_]+", "github_pat_***", text)
    text = re.sub(r"(api-key=)[^&\s\"']+", r"\1***", text)
    text = re.sub(r"(x-access-token:)[^@\s]+", r"\1***", text)
    return text


def sh(cmd: str, timeout=20) -> str:
    try:
        return subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=timeout).stdout.strip()
    except Exception as e:
        return f"(fout: {e})"


def tail(path: str, n: int) -> str:
    try:
        with open(path, errors="replace") as f:
            return "".join(f.readlines()[-n:]).rstrip()
    except FileNotFoundError:
        return "(bestand bestaat niet)"


def health() -> str:
    try:
        with urllib.request.urlopen("http://127.0.0.1:8080/health", timeout=4) as r:
            return r.read().decode()
    except urllib.error.HTTPError as e:
        return e.read().decode(errors="replace")
    except Exception as e:
        return f"(niet bereikbaar: {e})"


def build(note: str) -> str:
    now = time.strftime("%Y-%m-%d %H:%M:%S UTC", time.gmtime())
    disk = sh("df -h / | tail -1 | awk '{print $3 \"/\" $2}'")
    mem = sh("free -m | awk '/Mem/{print $3 \"/\" $2 \" MB\"}'")
    rev = sh("git -C " + BOT_DIR + " rev-parse --short HEAD 2>/dev/null") or "(geen repo)"
    parts = [
        f"# Schaduwbot status\n",
        f"- tijd: {now}",
        f"- melding: {note}",
        f"- host: {socket.gethostname()} | uptime: {sh('uptime -p')}",
        f"- bot-service: {sh('systemctl is-active schaduwbot')}",
        f"- code-versie: {rev}",
        f"- schijf: {disk} | geheugen: {mem}",
        "\n## Health\n```json", health(), "```",
        "\n## Laatste rapport\n```", tail(f"{BOT_DIR}/reports/latest.md", 60), "```",
        "\n## Bot-log (laatste 80 regels)\n```", sh("journalctl -u schaduwbot -n 80 --no-pager 2>/dev/null"), "```",
        "\n## Update-log (laatste 20 regels)\n```", tail("/var/log/schaduwbot-update.log", 20), "```",
        "\n## Analyses (laatste 25 regels)\n```", sh("systemctl is-active schaduwbot-wallets 2>/dev/null"), tail(f"{BOT_DIR}/reports/wallets.log", 25), "```",
        "\n## Bootstrap-log (laatste 60 regels)\n```", tail("/var/log/schaduwbot-bootstrap.log", 60), "```",
        "\n## cloud-init (laatste 25 regels)\n```", tail("/var/log/cloud-init-output.log", 25), "```",
    ]
    return redact("\n".join(parts)) + "\n"


def gh(method: str, path: str, body=None):
    req = urllib.request.Request(API + path, method=method, data=json.dumps(body).encode() if body is not None else None)
    req.add_header("Authorization", f"Bearer {TOKEN}")
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("User-Agent", "schaduwbot-status")
    if body is not None:
        req.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            return r.status, json.loads(r.read().decode() or "{}")
    except urllib.error.HTTPError as e:
        try:
            return e.code, json.loads(e.read().decode() or "{}")
        except Exception:
            return e.code, {}


def git_blob_sha(data: bytes) -> str:
    return hashlib.sha1(b"blob %d\0" % len(data) + data).hexdigest()


def ensure_branch() -> bool:
    code, _ = gh("GET", f"/repos/{REPO}/git/ref/heads/{BRANCH}")
    if code == 200:
        return True
    code, main = gh("GET", f"/repos/{REPO}/git/ref/heads/main")
    if code != 200:
        print("main-branch niet gevonden:", code, main.get("message"))
        return False
    code, res = gh("POST", f"/repos/{REPO}/git/refs", {"ref": f"refs/heads/{BRANCH}", "sha": main["object"]["sha"]})
    if code not in (200, 201, 422):
        print("status-branch aanmaken mislukt:", code, res.get("message"))
        return False
    return True


def put_file(path: str, data: bytes, message: str) -> None:
    code, cur = gh("GET", f"/repos/{REPO}/contents/{path}?ref={BRANCH}")
    sha = cur.get("sha") if code == 200 else None
    if sha and sha == git_blob_sha(data):
        return
    body = {"message": message, "content": base64.b64encode(data).decode(), "branch": BRANCH}
    if sha:
        body["sha"] = sha
    code, res = gh("PUT", f"/repos/{REPO}/contents/{path}", body)
    print(path, "->", code, "" if code in (200, 201) else res.get("message"))


def main():
    note = sys.argv[1] if len(sys.argv) > 1 else "tick"
    if not REPO or not TOKEN:
        print("GITHUB_REPO/GITHUB_TOKEN ontbreken")
        return
    if not ensure_branch():
        return
    stamp = time.strftime("%Y-%m-%d %H:%M UTC", time.gmtime())
    put_file("status.md", build(note).encode(), f"status {stamp}: {note}"[:120])
    rep = f"{BOT_DIR}/reports/{time.strftime('%Y-%m-%d', time.gmtime())}.json"
    if os.path.exists(rep):
        with open(rep, "rb") as f:
            put_file("report.json", redact(f.read().decode(errors="replace")).encode(), f"rapport {stamp}")
    for name in ("wallets.md", "wallets.json", "ledger.md", "ledger.json", "video_replay.md", "video_replay.json", "pumpswap.md", "pumpswap.json"):
        path = f"{BOT_DIR}/reports/{name}"
        if os.path.exists(path):
            with open(path, "rb") as f:
                put_file(name, redact(f.read().decode(errors="replace")).encode(), f"wallet-analyse {stamp}")


if __name__ == "__main__":
    main()
