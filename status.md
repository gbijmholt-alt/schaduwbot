# Schaduwbot status

- tijd: 2026-09-10 13:48:47 UTC
- melding: bootstrap klaar
- host: ubuntu-4gb-fsn1-1 | uptime: up 1 minute
- bot-service: active
- code-versie: 5d6c187
- schijf: 1.7G/38G | geheugen: 510/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.1, "uptime_s": 30, "tokens_in_memory": 9, "msgs": 7614, "trades": 111, "creates": 9, "decode_fail": 35, "rpc_calls": 3, "rpc_errors": 2, "sol_usd": 99.72300912402481, "open_positions": 0}
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
```

## Bootstrap-log (laatste 60 regels)
```
Preparing to unpack …/06-curl_8.18.0-1ubuntu2.5_amd64.deb…
Unpacking curl (8.18.0-1ubuntu2.5) over (8.18.0-1ubuntu2.4)…
Preparing to unpack …/07-libcurl4t64_8.18.0-1ubuntu2.5_amd64.deb…
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
```

## cloud-init (laatste 25 regels)
```
ci-info: +--------+------+-----------------------------+-----------------+--------+-------------------+
ci-info: +++++++++++++++++++++++++++++Route IPv4 info++++++++++++++++++++++++++++++
ci-info: +-------+-------------+------------+-----------------+-----------+-------+
ci-info: | Route | Destination |  Gateway   |     Genmask     | Interface | Flags |
ci-info: +-------+-------------+------------+-----------------+-----------+-------+
ci-info: |   0   |   0.0.0.0   | 172.31.1.1 |     0.0.0.0     |    eth0   |   UG  |
ci-info: |   1   |  172.31.1.1 |  0.0.0.0   | 255.255.255.255 |    eth0   |   UH  |
ci-info: |   2   | 185.12.64.1 | 172.31.1.1 | 255.255.255.255 |    eth0   |  UGH  |
ci-info: |   3   | 185.12.64.2 | 172.31.1.1 | 255.255.255.255 |    eth0   |  UGH  |
ci-info: +-------+-------------+------------+-----------------+-----------+-------+
ci-info: +++++++++++++++++++++++++Route IPv6 info+++++++++++++++++++++++++
ci-info: +-------+-------------------------+---------+-----------+-------+
ci-info: | Route |       Destination       | Gateway | Interface | Flags |
ci-info: +-------+-------------------------+---------+-----------+-------+
ci-info: |   0   | 2a01:4f8:c012:977d::/64 |    ::   |    eth0   |   U   |
ci-info: |   1   |        fe80::/64        |    ::   |    eth0   |   U   |
ci-info: |   2   |           ::/0          | fe80::1 |    eth0   |   UG  |
ci-info: |   4   |          local          |    ::   |    eth0   |   U   |
ci-info: |   5   |          local          |    ::   |    eth0   |   U   |
ci-info: |   6   |        multicast        |    ::   |    eth0   |   U   |
ci-info: +-------+-------------------------+---------+-----------+-------+
2026-09-10 13:47:18,097 - lifecycle.py[DEPRECATED]: Config key 'lists' is deprecated in 22.3 and scheduled to be removed in 27.3. Use 'users' instead.
2026-09-10 13:47:18,097 - lifecycle.py[DEPRECATED]: The chpasswd multiline string is deprecated in 22.2 and scheduled to be removed in 27.2. Use string type instead.
Cloud-init v. 26.1-0ubuntu3~26.04.1 running 'modules:config' at Thu, 10 Sep 2026 13:47:18 +0000. Up 21.70 seconds.
Cloud-init v. 26.1-0ubuntu3~26.04.1 running 'modules:final' at Thu, 10 Sep 2026 13:47:21 +0000. Up 24.36 seconds.
```
