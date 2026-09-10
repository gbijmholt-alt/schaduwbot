# Schaduwbot status

- tijd: 2026-09-10 14:10:17 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 23 minutes
- bot-service: active
- code-versie: 5d6c187
- schijf: 1.8G/38G | geheugen: 494/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 1320, "tokens_in_memory": 519, "msgs": 212442, "trades": 38467, "creates": 519, "decode_fail": 4421, "rpc_calls": 672, "rpc_errors": 94, "sol_usd": 99.49059656322275, "open_positions": 49}
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
Sep 10 13:58:47 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 13:58:47,998 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 13:58:48 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 13:58:48,086 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 13:58:48 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 13:58:48,295 main INFO screen JHI pass=0 dev=0.0 ins=40.9 pro=2 1a=False 1b=False 2=True (0.4s)
Sep 10 13:58:59 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 13:58:59,926 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 13:59:00 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 13:59:00,053 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 13:59:00 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 13:59:00,223 main INFO screen MON pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.3s)
Sep 10 13:59:04 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 13:59:04,422 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 13:59:04 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 13:59:04,551 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 13:59:05 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 13:59:05,215 main INFO screen USMS pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.9s)
Sep 10 13:59:13 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 13:59:13,018 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 13:59:13 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 13:59:13,145 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 13:59:13 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 13:59:13,306 main INFO screen HOOD pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 10 13:59:40 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 13:59:40,632 aiohttp.access INFO 127.0.0.1 [10/Sep/2026:13:59:40 +0000] "GET /health HTTP/1.1" 200 416 "-" "Python-urllib/3.14"
Sep 10 13:59:42 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 13:59:42,793 main INFO screen APEZCAT pass=0 dev=32.12 ins=0.35 pro=30 1a=False 1b=False 2=False (3.4s)
Sep 10 14:00:06 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:00:06,776 main INFO screen GOAT23 pass=0 dev=0.37 ins=0.0 pro=2 1a=False 1b=False 2=False (6.6s)
Sep 10 14:00:15 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:00:15,047 main INFO screen WTF pass=1 dev=0.0 ins=0.0 pro=29 1a=False 1b=False 2=False (3.0s)
Sep 10 14:00:46 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:00:46,573 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 14:00:46 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:00:46,699 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 14:00:51 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:00:51,645 main INFO screen VC pass=0 dev=0.0 ins=72.68 pro=1 1a=False 1b=False 2=True (5.1s)
Sep 10 14:00:55 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:00:55,132 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 14:00:55 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:00:55,263 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 14:00:59 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:00:59,774 main INFO screen BEAST pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (4.7s)
Sep 10 14:01:26 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:01:26,138 main INFO screen RESIGNED pass=0 dev=0.21 ins=0.0 pro=2 1a=False 1b=False 2=False (9.0s)
Sep 10 14:01:46 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:01:46,947 main INFO screen SFD pass=0 dev=10.44 ins=12.71 pro=26 1a=False 1b=False 2=False (5.6s)
Sep 10 14:01:53 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:01:53,467 main INFO screen RISE pass=0 dev=41.81 ins=0.0 pro=5 1a=False 1b=False 2=True (7.4s)
Sep 10 14:03:14 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:03:14,199 main INFO screen p pass=0 dev=0.35 ins=0.0 pro=2 1a=False 1b=False 2=False (7.9s)
Sep 10 14:03:23 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:03:23,469 main INFO screen FYC pass=1 dev=0.0 ins=13.57 pro=34 1a=False 1b=False 2=False (8.3s)
Sep 10 14:04:01 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:04:01,315 main INFO screen MISTAKE pass=1 dev=0.0 ins=0.0 pro=11 1a=False 1b=False 2=False (7.8s)
Sep 10 14:04:14 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:04:14,693 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 14:04:14 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:04:14,788 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 14:04:14 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:04:14,936 main INFO screen GRND pass=0 dev=0.0 ins=26.03 pro=5 1a=False 1b=False 2=True (0.3s)
Sep 10 14:05:10 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:05:10,926 aiohttp.access INFO 127.0.0.1 [10/Sep/2026:14:05:10 +0000] "GET /health HTTP/1.1" 200 416 "-" "Python-urllib/3.14"
Sep 10 14:05:17 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:05:17,100 main INFO screen p pass=0 dev=0.18 ins=0.0 pro=2 1a=False 1b=False 2=False (7.6s)
Sep 10 14:05:27 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:05:27,775 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 14:05:27 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:05:27,872 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 14:05:28 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:05:28,032 main INFO screen GAY pass=0 dev=0.0 ins=17.79 pro=16 1a=False 1b=False 2=True (0.4s)
Sep 10 14:05:33 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:05:33,810 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 14:05:33 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:05:33,942 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 14:05:34 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:05:34,220 main INFO screen GAYLANA pass=0 dev=0.0 ins=37.58 pro=1 1a=False 1b=False 2=True (0.5s)
Sep 10 14:05:34 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:05:34,314 main INFO screen WC pass=0 dev=0.3 ins=0.0 pro=3 1a=False 1b=False 2=False (6.2s)
Sep 10 14:06:17 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:06:17,475 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 14:06:17 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:06:17,598 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 14:06:21 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:06:21,315 main INFO screen $TRUMP pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (3.9s)
Sep 10 14:06:40 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:06:40,895 main INFO screen BBS pass=0 dev=0.7 ins=0.0 pro=2 1a=False 1b=False 2=False (8.6s)
Sep 10 14:06:57 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:06:57,967 main INFO screen FIRED pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (7.7s)
Sep 10 14:07:07 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:07:07,319 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 14:07:07 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:07:07,446 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 14:07:12 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:07:12,629 main INFO screen baton pass=0 dev=0.0 ins=79.31 pro=2 1a=False 1b=False 2=True (5.4s)
Sep 10 14:07:17 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:07:17,641 main INFO screen Syd pass=0 dev=0.21 ins=0.0 pro=5 1a=False 1b=False 2=False (10.3s)
Sep 10 14:07:21 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:07:21,761 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 14:07:21 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:07:21,863 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 14:07:27 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:07:27,680 main INFO screen PUSSY pass=0 dev=0.0 ins=79.27 pro=1 1a=False 1b=False 2=True (6.0s)
Sep 10 14:07:27 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:07:27,813 main INFO screen GAY pass=1 dev=0.0 ins=0.88 pro=28 1a=False 1b=False 2=False (2.2s)
Sep 10 14:08:07 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:08:07,155 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 14:08:07 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:08:07,247 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 14:08:07 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:08:07,627 main INFO screen GAY pass=0 dev=0.0 ins=18.84 pro=26 1a=False 1b=False 2=True (0.6s)
Sep 10 14:08:09 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:08:09,045 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 14:08:09 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:08:09,299 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 14:08:12 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:08:12,948 main INFO screen $BAIFLASH pass=0 dev=0.0 ins=0.04 pro=1 1a=False 1b=False 2=True (4.1s)
Sep 10 14:08:14 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:08:14,179 main INFO screen p pass=0 dev=0.35 ins=0.0 pro=2 1a=False 1b=False 2=False (6.7s)
Sep 10 14:08:16 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:08:16,011 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 14:08:16 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:08:16,139 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 14:08:16 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:08:16,453 main INFO screen GAY pass=0 dev=0.0 ins=25.74 pro=6 1a=False 1b=False 2=True (0.5s)
Sep 10 14:08:31 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:08:31,289 main INFO screen MoM pass=0 dev=0.88 ins=0.0 pro=1 1a=False 1b=False 2=False (9.6s)
Sep 10 14:08:35 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:08:35,832 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 14:08:35 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:08:35,944 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 14:08:36 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:08:36,098 main INFO screen HOMO pass=0 dev=0.0 ins=13.57 pro=17 1a=False 1b=False 2=True (0.4s)
Sep 10 14:08:41 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:08:41,414 main INFO screen monkey  pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (8.2s)
Sep 10 14:08:41 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:08:41,515 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 14:08:41 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:08:41,600 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 14:08:45 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:08:45,124 main INFO screen DOOYET pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (3.7s)
Sep 10 14:08:52 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:08:52,624 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 14:08:52 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:08:52,867 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 14:08:53 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:08:53,143 main INFO screen HOMO pass=0 dev=0.0 ins=38.31 pro=3 1a=False 1b=False 2=True (0.6s)
Sep 10 14:08:59 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:08:59,598 main INFO screen THINK pass=0 dev=0.1 ins=0.0 pro=1 1a=False 1b=False 2=False (7.0s)
Sep 10 14:09:04 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:09:04,847 aiohttp.access INFO 16.5.0.236 [10/Sep/2026:14:09:04 +0000] "GET / HTTP/1.1" 404 193 "-" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0"
Sep 10 14:09:17 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:09:17,066 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 14:09:17 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:09:17,166 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 14:09:17 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:09:17,378 main INFO screen GRND pass=0 dev=0.0 ins=24.92 pro=10 1a=False 1b=False 2=True (0.4s)
Sep 10 14:10:17 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:10:17,457 aiohttp.access INFO 127.0.0.1 [10/Sep/2026:14:10:17 +0000] "GET /health HTTP/1.1" 200 417 "-" "Python-urllib/3.14"
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
