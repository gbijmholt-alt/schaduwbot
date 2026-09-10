# Schaduwbot status

- tijd: 2026-09-10 14:25:37 UTC
- melding: tick
- host: ubuntu-4gb-fsn1-1 | uptime: up 38 minutes
- bot-service: active
- code-versie: 5d6c187
- schijf: 1.8G/38G | geheugen: 501/3814 MB

## Health
```json
{"ok": true, "last_event_age_s": 0.1, "uptime_s": 2240, "tokens_in_memory": 796, "msgs": 334289, "trades": 64140, "creates": 796, "decode_fail": 6584, "rpc_calls": 1108, "rpc_errors": 133, "sol_usd": 100.05880098233575, "open_positions": 48}
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
Sep 10 14:10:29 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:10:29,261 main INFO screen MONARK pass=0 dev=0.0 ins=6.47 pro=77 1a=False 1b=False 2=True (7.1s)
Sep 10 14:11:19 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:11:19,807 main INFO screen NUTFLIX pass=1 dev=0.0 ins=0.0 pro=37 1a=False 1b=False 2=False (7.2s)
Sep 10 14:12:02 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:12:02,942 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 14:12:03 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:12:03,056 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 14:12:08 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:12:08,881 main INFO screen NETFLICKS pass=0 dev=0.0 ins=0.0 pro=2 1a=False 1b=False 2=True (6.0s)
Sep 10 14:12:44 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:12:44,100 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 14:12:44 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:12:44,209 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 14:12:49 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:12:49,334 main INFO screen batomo pass=0 dev=0.0 ins=79.24 pro=9 1a=False 1b=False 2=True (5.3s)
Sep 10 14:13:06 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:13:06,057 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 14:13:06 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:13:06,158 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 14:13:12 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:13:12,473 main INFO screen ND4 pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (6.5s)
Sep 10 14:13:19 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:13:19,714 main INFO screen WC pass=0 dev=0.33 ins=0.0 pro=2 1a=False 1b=False 2=False (8.2s)
Sep 10 14:13:51 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:13:51,962 main INFO screen LMAO pass=0 dev=0.0 ins=0.0 pro=3 1a=False 1b=False 2=False (9.6s)
Sep 10 14:13:58 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:13:58,167 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 14:13:58 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:13:58,275 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 14:14:01 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:14:01,892 main INFO screen ASTRA pass=0 dev=0.0 ins=77.07 pro=6 1a=False 1b=False 2=True (3.8s)
Sep 10 14:14:10 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:14:10,352 main INFO screen KIRK pass=0 dev=0.35 ins=0.0 pro=2 1a=False 1b=False 2=False (6.6s)
Sep 10 14:14:28 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:14:28,411 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 14:14:28 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:14:28,557 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 14:14:28 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:14:28,742 main INFO screen PAIRS pass=0 dev=0.0 ins=40.1 pro=2 1a=False 1b=False 2=True (0.4s)
Sep 10 14:14:38 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:14:38,435 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 14:14:38 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:14:38,562 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 14:14:42 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:14:42,728 main INFO screen IMON pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (4.4s)
Sep 10 14:14:46 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:14:46,163 main INFO screen holyfrog pass=0 dev=0.0 ins=0.0 pro=13 1a=False 1b=False 2=True (2.1s)
Sep 10 14:15:00 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:15:00,688 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 14:15:00 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:15:00,797 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 14:15:01 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:15:01,165 main INFO screen pairs pass=1 dev=0.0 ins=9.16 pro=21 1a=False 1b=False 2=False (0.6s)
Sep 10 14:15:19 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:15:19,279 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 14:15:19 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:15:19,392 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 14:15:20 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:15:20,239 aiohttp.access INFO 127.0.0.1 [10/Sep/2026:14:15:20 +0000] "GET /health HTTP/1.1" 200 418 "-" "Python-urllib/3.14"
Sep 10 14:15:24 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:15:24,458 main INFO screen PENPE pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (5.3s)
Sep 10 14:16:31 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:16:31,362 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 14:16:31 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:16:31,743 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 14:16:31 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:16:31,795 main INFO screen GRND pass=1 dev=0.0 ins=0.0 pro=19 1a=False 1b=False 2=False (0.5s)
Sep 10 14:16:31 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:16:31,915 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 14:16:35 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:16:35,663 main INFO screen SGLD pass=1 dev=0.0 ins=4.4 pro=43 1a=False 1b=False 2=False (4.0s)
Sep 10 14:16:36 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:16:36,978 main INFO screen MISTAKE pass=1 dev=0.0 ins=0.0 pro=12 1a=False 1b=False 2=False (4.7s)
Sep 10 14:18:52 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:18:52,669 main INFO screen Chud pass=0 dev=0.35 ins=0.0 pro=3 1a=False 1b=False 2=False (7.4s)
Sep 10 14:18:54 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:18:54,511 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 14:18:54 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:18:54,588 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 14:19:00 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:19:00,539 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 14:19:00 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:19:00,677 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 14:19:01 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:19:01,415 main INFO screen PLUSHY pass=0 dev=0.0 ins=39.67 pro=1 1a=False 1b=False 2=True (7.2s)
Sep 10 14:19:05 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:19:05,364 main INFO screen kittylick pass=0 dev=0.21 ins=0.0 pro=2 1a=False 1b=False 2=False (8.1s)
Sep 10 14:19:07 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:19:07,175 main INFO screen WOFI pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (6.7s)
Sep 10 14:19:15 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:19:15,531 main INFO screen STONKFLY pass=1 dev=0.0 ins=17.82 pro=25 1a=False 1b=False 2=False (7.5s)
Sep 10 14:19:32 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:19:32,246 main INFO screen FYJ pass=0 dev=0.32 ins=0.0 pro=1 1a=False 1b=False 2=False (7.2s)
Sep 10 14:19:35 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:19:35,095 main INFO screen WAGMI pass=1 dev=0.9 ins=0.0 pro=46 1a=False 1b=False 2=False (7.0s)
Sep 10 14:19:35 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:19:35,205 main INFO screen holyfrog pass=0 dev=0.0 ins=0.0 pro=16 1a=False 1b=False 2=True (2.5s)
Sep 10 14:20:20 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:20:20,536 aiohttp.access INFO 127.0.0.1 [10/Sep/2026:14:20:20 +0000] "GET /health HTTP/1.1" 200 418 "-" "Python-urllib/3.14"
Sep 10 14:20:59 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:20:59,729 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 14:20:59 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:20:59,811 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 14:21:04 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:21:04,495 main INFO screen MrBeast pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (4.9s)
Sep 10 14:21:43 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:21:43,985 main INFO screen GAYTJR pass=0 dev=40.26 ins=0.0 pro=3 1a=False 1b=False 2=True (7.1s)
Sep 10 14:22:14 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:22:14,444 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 14:22:14 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:22:14,540 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 14:22:23 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:22:23,145 main INFO screen HETERO pass=0 dev=0.0 ins=13.46 pro=23 1a=False 1b=False 2=True (8.8s)
Sep 10 14:22:41 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:22:41,419 main INFO screen sol pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (6.8s)
Sep 10 14:23:12 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:23:12,701 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 14:23:12 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:23:12,805 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 14:23:19 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:23:19,125 main INFO screen USWR pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (6.5s)
Sep 10 14:23:39 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:23:39,595 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 14:23:39 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:23:39,741 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 14:23:42 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:23:42,936 main INFO screen DERP pass=0 dev=0.21 ins=0.0 pro=1 1a=False 1b=False 2=False (8.6s)
Sep 10 14:23:45 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:23:45,176 main INFO screen JUGGERNAUT pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (5.6s)
Sep 10 14:23:50 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:23:50,135 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 14:23:50 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:23:50,272 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 14:23:55 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:23:55,833 main INFO screen LAPTRUMP pass=0 dev=0.0 ins=77.54 pro=5 1a=False 1b=False 2=True (5.8s)
Sep 10 14:24:03 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:24:03,755 main INFO screen FAG pass=1 dev=0.0 ins=6.1 pro=28 1a=False 1b=False 2=False (4.1s)
Sep 10 14:24:05 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:24:05,145 main INFO screen IMON pass=0 dev=0.33 ins=0.0 pro=1 1a=False 1b=False 2=False (8.1s)
Sep 10 14:24:05 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:24:05,935 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 14:24:06 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:24:06,042 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 14:24:07 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:24:07,016 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 14:24:07 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:24:07,130 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 14:24:09 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:24:09,969 main INFO screen musk pass=0 dev=0.0 ins=23.84 pro=10 1a=False 1b=False 2=True (4.1s)
Sep 10 14:24:11 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:24:11,245 main INFO screen HOOD pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (4.3s)
Sep 10 14:24:55 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:24:55,753 rpc WARNING rpc getTokenLargestAccounts error {'code': -32602, 'message': 'Invalid param: not a Token mint'}
Sep 10 14:24:55 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:24:55,839 rpc WARNING rpc getTokenAccountsByOwner error {'code': -32602, 'message': 'Error getting token program id and mint: Invalid param: could not find mint'}
Sep 10 14:25:00 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:25:00,767 main INFO screen Starbucks pass=0 dev=0.0 ins=0.0 pro=1 1a=False 1b=False 2=True (5.1s)
Sep 10 14:25:37 ubuntu-4gb-fsn1-1 python[2122]: 2026-09-10 14:25:37,121 aiohttp.access INFO 127.0.0.1 [10/Sep/2026:14:25:37 +0000] "GET /health HTTP/1.1" 200 420 "-" "Python-urllib/3.14"
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
