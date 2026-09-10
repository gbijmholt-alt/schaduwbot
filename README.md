# Schaduwbot — fase 1

Meet of de memecoin-scalpstrategie uit de video (pump.fun, dip-vanaf-ATH, houder- en bundle-checks) na kosten een positieve verwachtingswaarde heeft. **Er wordt niets gehandeld**: geen wallet, geen sleutel, alleen virtuele trades tegen echte prijzen. Specificatie: `Fase1_Schaduwbot_Bouwplan.docx`.

## Werking

```
Solana websocket (logsSubscribe op pump.fun-programma)
  └─ decoder.py      CreateEvent / TradeEvent / CompleteEvent uit "Program data:"
     └─ state.py     reserves, prijs, ATH, kopers, creator-positie, rug-detectie
        ├─ filters   New pairs ≥ $7k  |  Final stretch: curve ≥ 70%, ≤ 40 min, $8k–$30k
        ├─ screening.py (eenmalig, async)  top-5 saldi & funding-datum, bundle-patroon,
        │                                   dev-%, insiders-%, pro-traders-proxy, X-link, RugCheck
        └─ simulator.py  dip 35/40/45% ➜ herstel ➜ fill na 2 s ➜ V1/V2/V3 ➜ fill na 2 s
                          slippage exact via bonding curve; fees pump 1,25% + Axiom 0,855% / PP 0,5% + prio
store.py (SQLite)  ➜ report.py (funnel, winkans, rug-%, EV, drawdown, Monte Carlo) ➜ reports/latest.md
health.py          GET :8080/health  (UptimeRobot)   GET :8080/latest (rapport)
```

Tokens die filter A nooit halen worden niet gesimuleerd. Tokens die filter A halen worden **altijd** gesimuleerd, ook als de screening faalt — zo meten we of de checks waarde toevoegen (`screen_pass` 1/0 in `sim_trades`).

## Commando's

```
python main.py run        # 24/7 (systemd)
python main.py probe 60   # 60 s meeluisteren, decoder-sanity
python main.py report     # rapport uit de database
python tests/test_all.py      # unit tests (decoder, curve, simulator)
```

## Deploy (Hetzner + GitHub, geen SSH nodig)

1. `deploy/cloud-init.yaml` met drie ingevulde waarden in het veld *Cloud config* bij het aanmaken van de server.
2. Server kloont deze repo, installeert, start `schaduwbot.service`.
3. `schaduwbot-update.timer` (elke 5 min): pusht `health.json`, `latest.md`, `log-tail.txt`, `heartbeat.txt` naar branch **`status`**; haalt nieuwe code van `main` op en herstart bij wijziging.

Alle parameters staan in `bot/config.py` en zijn via `.env` te overschrijven.

## Bekende benaderingen (zie bouwplan §2 en §8)

- "Final stretch" en "pro traders" zijn Axiom-labels zonder publieke definitie → benaderd.
- Community-check op X wordt niet gemeten; X-link-aanwezigheid en unieke kopers worden gelogd.
- Schaduwfills zijn een bovengrens: mislukte transacties en MEV zitten er niet in.
