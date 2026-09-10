# Schaduwbot status

- tijd: 2026-09-10 13:54:40 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 7 minutes
- bot-service: active
- code-versie: 5d6c187
- schijf: 1.7G/38G | geheugen: 476/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 383, "tokens_in_memory": 179, "msgs": 52385, "trades": 8685, "creates": 179, "decode_fail": 1179, "rpc_calls": 193, "rpc_errors": 36, "sol_usd": 99.80758592504672, "open_positions": 10}
```

## Laatste rapport
```
# Schaduwbot rapport — 2026-09-10 13:48 UTC

Gelogde schaduwtrades: **0**

## Funnel per dag

| dag | created | newpairs | final_stretch | screened | screen_pass | entry | exit |
|---|---|---|---|---|---|---|---|

## Varianten (inzet 0,2 SOL, PumpPortal-fees)

| variant | n | winkans | rug% | gem. winst | gem. verlies | EV/trade | maxDD@20% |
|---|---|---|---|---|---|---|---|

_Nog geen variant met ≥ 30 trades._
```

## Bot-log (laatste 80 regels)
```
Sep 10 13:48:16 ubuntu-4gb-fsn1-1 systemd[1]: Started schaduwbot.service - Schaduwbot (fase 1, geen echte trades).
Sep 10 13:48:17 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 13:48:17,531 main INFO verbonden met wss://mainnet.helius-rpc.com/
Sep 10 13:48:19 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 13:48:19,112 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 13:48:19 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 13:48:19,209 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 13:48:19 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 13:48:19,438 main INFO screen URMOM pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 10 13:48:47 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 13:48:47,390 aiohttp.access INFO 127.0.0.1 [10/Sep/2026:13:48:47 +0000] "GET /health HTTP/1.1" 200 401 "-" "Python-urllib/3.14"
Sep 10 13:49:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 13:49:37,069 aiohttp.access INFO 127.0.0.1 [10/Sep/2026:13:49:37 +0000] "GET /health HTTP/1.1" 200 405 "-" "Python-urllib/3.14"
Sep 10 13:50:17 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 13:50:17,332 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 13:50:17 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 13:50:17,428 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 13:50:17 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 13:50:17,636 main INFO screen BARRON pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 10 13:50:29 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 13:50:29,814 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 13:50:29 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 13:50:29,939 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 13:50:30 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 13:50:30,103 main INFO screen BAPEPE pass=0 dev=0.0 ins=79.23 pro=7 1a=False 1b=False 2=True (0.4s)
Sep 10 13:50:42 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 13:50:42,853 main INFO screen WEPSTEIN pass=0 dev=0.35 ins=0.0 pro=2 1a=False 1b=False 2=False (2.8s)
Sep 10 13:51:15 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 13:51:15,115 main INFO screen CONNE pass=0 dev=0.05 ins=0.0 pro=1 1a=False 1b=False 2=False (1.8s)
Sep 10 13:51:21 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 13:51:21,152 main INFO screen SCRVAN pass=0 dev=2.55 ins=0.0 pro=2 1a=False 1b=False 2=False (2.3s)
Sep 10 13:51:30 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 13:51:30,718 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 13:51:30 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 13:51:30,843 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 13:51:30 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 13:51:30,966 main INFO screen $Kirk pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (0.3s)
Sep 10 13:51:35 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 13:51:35,596 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 13:51:35 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 13:51:35,774 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 13:51:36 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 13:51:36,073 main INFO screen resigned pass=1 dev=0.0 ins=10.31 pro=24 1a=False 1b=False 2=False (0.5s)
Sep 10 13:51:40 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 13:51:40,854 main INFO screen 4D pass=1 dev=0.0 ins=0.37 pro=38 1a=False 1b=False 2=False (2.7s)
Sep 10 13:51:41 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 13:51:41,030 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 13:51:41 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 13:51:41,148 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 13:51:41 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 13:51:41,298 main INFO screen CKRK pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.3s)
Sep 10 13:51:41 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 13:51:41,988 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 13:51:42 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 13:51:42,102 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 13:51:42 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 13:51:42,235 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 13:51:42 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 13:51:42,384 main INFO screen STONKFLY pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.5s)
Sep 10 13:51:42 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 13:51:42,475 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 13:51:42 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 13:51:42,622 main INFO screen FERSPE pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.6s)
Sep 10 13:51:52 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 13:51:52,403 main INFO screen MUK pass=1 dev=0.0 ins=18.19 pro=28 1a=False 1b=False 2=False (1.4s)
Sep 10 13:52:02 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 13:52:02,899 main INFO screen kittylick pass=0 dev=1.72 ins=0.0 pro=2 1a=False 1b=False 2=False (2.1s)
Sep 10 13:52:08 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 13:52:08,917 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 13:52:09 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 13:52:09,011 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 13:52:09 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 13:52:09,351 main INFO screen resigned pass=0 dev=0.0 ins=32.22 pro=8 1a=False 1b=False 2=True (0.5s)
Sep 10 13:52:23 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 13:52:23,153 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 13:52:23 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 13:52:23,277 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 13:52:23 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 13:52:23,451 main INFO screen Clanker pass=1 dev=0.0 ins=11.38 pro=18 1a=False 1b=False 2=False (0.4s)
Sep 10 13:52:34 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 13:52:34,228 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 13:52:34 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 13:52:34,344 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 13:52:34 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 13:52:34,505 main INFO screen $CAT pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.4s)
Sep 10 13:52:36 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 13:52:36,551 main INFO screen PC pass=0 dev=0.37 ins=0.0 pro=1 1a=False 1b=False 2=False (1.9s)
Sep 10 13:52:42 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 13:52:42,086 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 13:52:42 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 13:52:42,249 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 13:52:42 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 13:52:42,374 main INFO screen TWC pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (0.3s)
Sep 10 13:52:49 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 13:52:49,047 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 13:52:49 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 13:52:49,171 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 13:52:49 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 13:52:49,305 main INFO screen KIRK pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.3s)
Sep 10 13:53:10 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 13:53:10,872 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 13:53:10 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 13:53:10,921 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 13:53:11 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 13:53:11,162 main INFO screen MrBeast pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 10 13:53:11 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 13:53:11,449 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 13:53:11 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 13:53:11,576 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 13:53:11 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 13:53:11,724 main INFO screen Elon pass=0 dev=0.0 ins=32.39 pro=9 1a=False 1b=False 2=True (0.3s)
Sep 10 13:53:40 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 13:53:40,237 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 13:53:40 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 13:53:40,332 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 13:53:40 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 13:53:40,533 main INFO screen BARRET pass=0 dev=0.0 ins=20.74 pro=13 1a=False 1b=False 2=True (0.4s)
Sep 10 13:54:16 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 13:54:16,234 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 13:54:16 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 13:54:16,333 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 13:54:16 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 13:54:16,692 main INFO screen chud pass=0 dev=0.0 ins=13.89 pro=31 1a=False 1b=False 2=True (0.6s)
Sep 10 13:54:31 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 13:54:31,896 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 13:54:31 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 13:54:31,988 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 13:54:32 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 13:54:32,183 main INFO screen BATONSZN pass=0 dev=0.0 ins=77.77 pro=10 1a=False 1b=False 2=True (0.4s)
Sep 10 13:54:39 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 13:54:39,237 main INFO screen p pass=0 dev=0.18 ins=0.0 pro=3 1a=False 1b=False 2=False (3.2s)
Sep 10 13:54:40 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 13:54:40,650 aiohttp.access INFO 127.0.0.1 [10/Sep/2026:13:54:40 +0000] "GET /health HTTP/1.1" 200 414 "-" "Python-urllib/3.14"
```

## Bootstrap-log (laatste 60 regels)
```
Unpacking libcurl4t64:amd64 (8.18.0-1ubuntu2.5) over (8.18.0-1ubuntu2.4)…
Preparing to unpack …/08-libcurl3t64-gnutls_8.18.0-1ubuntu2.5_amd64.deb…
Unpacking libcurl3t64-gnutls:amd64 (8.18.0-1ubuntu2.5) over (8.18.0-1ubuntu2.4)…
Selecting previously unselected package python3-wheel.
Preparing to unpack …/09-python3-wheel_0.46.3-2_all.deb…
Unpacking python3-wheel (0.46.3-2)…
Selecting previously unselected package python3-pip.
Preparing to unpack …/10-python3-pip_25.1.1+dfsg-1ubuntu2_all.deb…
Unpacking python3-pip (25.1.1+dfsg-1ubuntu2)…
Selecting previously unselected package python3-pip-whl.
Preparing to unpack …/11-python3-pip-whl_25.1.1+dfsg-1ubuntu2_all.deb…
Unpacking python3-pip-whl (25.1.1+dfsg-1ubuntu2)…
Selecting previously unselected package python3-setuptools-whl.
Preparing to unpack …/12-python3-setuptools-whl_78.1.1-0.1build1_all.deb…
Unpacking python3-setuptools-whl (78.1.1-0.1build1)…
Selecting previously unselected package python3.14-venv.
Preparing to unpack …/13-python3.14-venv_3.14.4-1ubuntu0.2_amd64.deb…
Unpacking python3.14-venv (3.14.4-1ubuntu0.2)…
Selecting previously unselected package python3-venv.
Preparing to unpack …/14-python3-venv_3.14.3-0ubuntu2_amd64.deb…
Unpacking python3-venv (3.14.3-0ubuntu2)…
Setting up python3-setuptools-whl (78.1.1-0.1build1)…
Setting up libcurl4t64:amd64 (8.18.0-1ubuntu2.5)…
Setting up python3-pip-whl (25.1.1+dfsg-1ubuntu2)…
Setting up libpython3.14-minimal:amd64 (3.14.4-1ubuntu0.2)…
Setting up libcurl3t64-gnutls:amd64 (8.18.0-1ubuntu2.5)…
Setting up python3-wheel (0.46.3-2)…
Setting up python3.14-gdbm (3.14.4-1ubuntu0.2)…
Setting up python3-pip (25.1.1+dfsg-1ubuntu2)…
Setting up curl (8.18.0-1ubuntu2.5)…
Setting up python3.14-minimal (3.14.4-1ubuntu0.2)…
Setting up libpython3.14-stdlib:amd64 (3.14.4-1ubuntu0.2)…
Setting up libpython3.14:amd64 (3.14.4-1ubuntu0.2)…
Setting up python3.14 (3.14.4-1ubuntu0.2)…
Setting up python3.14-venv (3.14.4-1ubuntu0.2)…
Setting up python3-venv (3.14.3-0ubuntu2)…
Processing triggers for systemd (259.5-0ubuntu3.4)…
Processing triggers for man-db (2.13.1-1build1)…
Processing triggers for libc-bin (2.43-2ubuntu2.3)…

Running kernel seems to be up-to-date.

Restarting services...
 systemctl restart packagekit.service

Service restarts being deferred:
 systemctl restart cloud-init-main.service
 systemctl restart networkd-dispatcher.service
 systemctl restart unattended-upgrades.service

No containers need to be restarted.

No user sessions are running outdated binaries.

No VM guests are running outdated hypervisor (qemu) binaries on this host.
Created symlink '/etc/systemd/system/multi-user.target.wants/schaduwbot.service' → '/etc/systemd/system/schaduwbot.service'.
install klaar
status.md -> 200 
report.json -> 201 
===== bootstrap klaar 2026-09-10T13:48:49Z =====
```

## cloud-init (laatste 25 regels)
```
|.BoBoB.          |
|  o.. +E         |
| .   .. S .      |
|.    . o =       |
| .  . + + .      |
| .+o . . o       |
| .**.            |
+----[SHA256]-----+
Generating public/private ed25519 key pair.
Your identification has been saved in /etc/ssh/ssh_host_ed25519_key
Your public key has been saved in /etc/ssh/ssh_host_ed25519_key.pub
The key fingerprint is:
SHA256:w2XLkdz/wp4oYdhzAWpZtAWfv0pFj8xAggp36PYfUQQ root@ubuntu-4gb-fsn1-1
The key's randomart image is:
+--[ED25519 256]--+
|       . oE++    |
|    . o o.oO..   |
|     + o +Bo= .  |
|      +.++.o.B o |
|     . oSoo. .B .|
|        o.* .o o |
|         o =. + .|
|          o. + o |
|           .o o  |
+----[SHA256]-----+
```
