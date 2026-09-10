# Schaduwbot status

- tijd: 2026-09-10 14:41:21 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 54 minutes
- bot-service: active
- code-versie: 5d6c187
- schijf: 1.8G/38G | geheugen: 520/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.0, "uptime_s": 3184, "tokens_in_memory": 1153, "msgs": 473683, "trades": 98716, "creates": 1153, "decode_fail": 9552, "rpc_calls": 1602, "rpc_errors": 179, "sol_usd": 100.1620410646649, "open_positions": 80}
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
Sep 10 14:26:52 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:26:52,347 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 14:26:52 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:26:52,431 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 14:26:52 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:26:52,756 main INFO screen shroom pass=0 dev=0.0 ins=39.07 pro=1 1a=False 1b=False 2=True (0.5s)
Sep 10 14:27:06 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:27:06,752 main INFO screen DZiEr pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (7.0s)
Sep 10 14:27:16 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:27:16,841 main INFO screen AIDRIVING pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (5.8s)
Sep 10 14:27:17 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:27:17,461 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 14:27:17 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:27:17,629 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 14:27:17 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:27:17,948 main INFO screen Pair pass=0 dev=0.0 ins=21.63 pro=7 1a=False 1b=False 2=True (0.5s)
Sep 10 14:28:01 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:28:01,010 main INFO screen wind pass=0 dev=3.39 ins=0.0 pro=3 1a=False 1b=False 2=False (6.4s)
Sep 10 14:28:09 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:28:09,826 main INFO screen BOF pass=0 dev=39.91 ins=0.0 pro=3 1a=False 1b=False 2=True (3.8s)
Sep 10 14:28:25 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:28:25,562 main INFO screen 30YEARS pass=0 dev=0.0 ins=23.18 pro=18 1a=False 1b=False 2=True (1.4s)
Sep 10 14:28:29 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:28:29,252 main INFO screen 30YEARS pass=0 dev=0.0 ins=24.05 pro=16 1a=False 1b=False 2=False (1.7s)
Sep 10 14:28:41 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:28:41,755 main INFO screen $BB pass=0 dev=0.26 ins=0.0 pro=1 1a=False 1b=False 2=False (2.2s)
Sep 10 14:28:46 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:28:46,402 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 14:28:46 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:28:46,526 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 14:28:46 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:28:46,884 main INFO screen SolFox pass=0 dev=0.0 ins=17.08 pro=14 1a=False 1b=False 2=True (0.6s)
Sep 10 14:29:19 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:29:19,574 main INFO screen $ASI pass=0 dev=0.09 ins=0.0 pro=2 1a=False 1b=False 2=False (2.4s)
Sep 10 14:29:54 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:29:54,627 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 14:29:54 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:29:54,678 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 14:29:55 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:29:55,021 main INFO screen HULKED pass=1 dev=0.0 ins=18.95 pro=16 1a=False 1b=False 2=False (0.5s)
Sep 10 14:30:17 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:30:17,748 main INFO screen BAGOFTITS pass=1 dev=0.0 ins=0.0 pro=36 1a=False 1b=False 2=False (3.8s)
Sep 10 14:30:28 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:30:28,686 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 14:30:28 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:30:28,806 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 14:30:28 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:30:28,952 main INFO screen HOOD pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.3s)
Sep 10 14:30:36 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:30:36,959 aiohttp.access INFO 127.0.0.1 [10/Sep/2026:14:30:36 +0000] "GET /health HTTP/1.1" 200 420 "-" "Python-urllib/3.14"
Sep 10 14:31:14 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:31:14,651 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 14:31:14 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:31:14,746 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 14:31:15 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:31:15,121 main INFO screen KIRK pass=1 dev=0.0 ins=17.37 pro=17 1a=False 1b=False 2=False (0.6s)
Sep 10 14:32:36 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:32:36,515 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 14:32:36 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:32:36,567 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 14:32:36 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:32:36,839 main INFO screen GROKCAT pass=0 dev=0.0 ins=6.67 pro=4 1a=False 1b=False 2=True (0.4s)
Sep 10 14:32:57 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:32:57,615 main INFO screen CUM pass=1 dev=0.0 ins=16.82 pro=50 1a=False 1b=False 2=False (2.7s)
Sep 10 14:34:10 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:34:10,738 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 14:34:10 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:34:10,841 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 14:34:11 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:34:11,035 main INFO screen RISE pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 10 14:34:27 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:34:27,409 main INFO screen $QPUMP  pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (2.6s)
Sep 10 14:34:27 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:34:27,545 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 14:34:27 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:34:27,691 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 14:34:27 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:34:27,898 main INFO screen CUM pass=0 dev=0.0 ins=18.35 pro=13 1a=False 1b=False 2=True (0.4s)
Sep 10 14:34:57 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:34:57,910 main INFO screen USMS pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (3.2s)
Sep 10 14:35:11 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:35:11,890 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 14:35:12 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:35:12,001 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 14:35:12 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:35:12,148 main INFO screen TRUMBATON pass=0 dev=0.0 ins=77.9 pro=10 1a=False 1b=False 2=True (0.3s)
Sep 10 14:36:01 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:36:01,317 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 14:36:01 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:36:01,391 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 14:36:01 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:36:01,758 main INFO screen CUM pass=0 dev=0.0 ins=13.31 pro=12 1a=False 1b=False 2=True (0.6s)
Sep 10 14:36:02 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:36:02,625 aiohttp.access INFO 127.0.0.1 [10/Sep/2026:14:36:02 +0000] "GET /health HTTP/1.1" 200 422 "-" "Python-urllib/3.14"
Sep 10 14:36:17 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:36:17,702 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 14:36:17 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:36:17,795 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 14:36:18 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:36:18,003 main INFO screen TOAD pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 10 14:36:26 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:36:26,669 main INFO screen $TBB pass=0 dev=0.26 ins=0.0 pro=1 1a=False 1b=False 2=False (2.7s)
Sep 10 14:36:36 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:36:36,656 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 14:36:36 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:36:36,746 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 14:36:36 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:36:36,901 main INFO screen 679 pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.3s)
Sep 10 14:37:17 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:37:17,320 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 14:37:17 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:37:17,433 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 14:37:17 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:37:17,614 main INFO screen PC pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 10 14:37:22 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:37:22,014 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 14:37:22 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:37:22,101 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 14:37:22 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:37:22,285 main INFO screen GROKCAT pass=0 dev=0.0 ins=2.19 pro=2 1a=False 1b=False 2=True (0.3s)
Sep 10 14:37:56 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:37:56,012 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 14:37:56 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:37:56,091 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 14:37:56 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:37:56,277 main INFO screen GOAF pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 10 14:37:58 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:37:58,930 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 14:37:59 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:37:59,056 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 14:37:59 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:37:59,218 main INFO screen DIH pass=0 dev=0.0 ins=10.33 pro=14 1a=False 1b=False 2=True (0.4s)
Sep 10 14:38:02 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:38:02,963 main INFO screen WC pass=0 dev=0.28 ins=0.0 pro=2 1a=False 1b=False 2=False (2.1s)
Sep 10 14:38:06 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:38:06,588 main INFO screen DMS pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=False (3.0s)
Sep 10 14:38:34 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:38:34,196 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 14:38:34 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:38:34,297 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 14:38:34 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:38:34,495 main INFO screen PC pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=False (0.4s)
Sep 10 14:38:55 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:38:55,380 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 14:38:55 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:38:55,479 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 14:38:55 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:38:55,672 main INFO screen TYGA pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (0.4s)
Sep 10 14:39:36 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:39:36,019 main INFO screen WC pass=0 dev=0.28 ins=0.0 pro=3 1a=False 1b=False 2=False (3.3s)
Sep 10 14:40:15 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:40:15,463 main INFO screen $BB pass=0 dev=0.25 ins=0.0 pro=1 1a=False 1b=False 2=False (2.2s)
Sep 10 14:40:25 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:40:25,957 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 14:40:26 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:40:26,101 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 14:40:26 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:40:26,236 main INFO screen FIX6900 pass=0 dev=0.0 ins=0.0 pro=23 1a=False 1b=False 2=True (0.4s)
Sep 10 14:41:21 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:41:21,715 aiohttp.access INFO 127.0.0.1 [10/Sep/2026:14:41:21 +0000] "GET /health HTTP/1.1" 200 421 "-" "Python-urllib/3.14"
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
