# Schaduwbot status

- tijd: 2026-09-10 13:47:25 UTC
- melding: bootstrap gestart
- host: ubuntu-4gb-fsn1-1 | uptime: up 0 minutes
- bot-service: inactive
- code-versie: (geen repo)
- schijf: 1.4G/38G | geheugen: 504/3814 MB

## Health
```json
(niet bereikbaar: <urlopen error [Errno 111] Connection refused>)
```

## Laatste rapport
```
(bestand bestaat niet)
```

## Bot-log (laatste 80 regels)
```
-- No entries --
```

## Bootstrap-log (laatste 60 regels)
```
===== bootstrap start 2026-09-10T13:47:22Z =====
Created symlink '/etc/systemd/system/timers.target.wants/schaduwbot-tick.timer' → '/etc/systemd/system/schaduwbot-tick.timer'.
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
