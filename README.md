# Schaduwbot — fase 1

Meet of de memecoin-scalpstrategie uit de video (pump.fun, dip-vanaf-ATH, houder- en bundle-checks) na kosten een positieve verwachtingswaarde heeft. **Er wordt niets gehandeld**: geen wallet, geen sleutel, alleen virtuele trades tegen echte prijzen. Specificatie: `Fase1_Schaduwbot_Bouwplan.docx`.

Alle bestanden staan plat in één map (geen submappen) zodat een upload via de GitHub-website altijd goed gaat.

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
health.py          GET :8080/health  (lokaal, op de server zelf)
status_push.py      elke 5 min: status.md + report.json naar GitHub-branch 'status' (geheimen weggelakt)
```

Tokens die filter A nooit halen worden niet gesimuleerd. Tokens die filter A halen worden **altijd** gesimuleerd, ook als de screening faalt — zo meten we of de checks waarde toevoegen (`screen_pass` 1/0 in `sim_trades`).

## Commando's

```
python3 main.py run        # 24/7 (systemd)
python3 main.py probe 60   # 60 s meeluisteren, decoder-sanity
python3 main.py report     # rapport uit de database
python3 test_all.py        # unit tests (decoder, curve, simulator)
```

## Deploy (Hetzner, zonder SSH of console)

1. `cloud-init.yaml` met drie ingevulde waarden (GitHub-gebruiker, GitHub-token, Helius-key) in het veld *Cloud config* bij het aanmaken van de server.
2. Dat bestand doet vrijwel niets zelf: het haalt alleen `bootstrap.sh` op en start het. Alle installatielogica — pakketten, git clone, venv, systemd — zit in `bootstrap.sh`, niet in de cloud-config. Dat houdt het cloud-config-veld kort en ongevoelig voor typefouten of een lastig toetsenbord in de Hetzner-console.
3. `bootstrap.sh` installeert **eerst** een timer (`schaduwbot-tick.timer`, elke 5 minuten) die `status_push.py` aanroept, en pas **daarna** de pakketten en de bot zelf. Gaat er ergens iets mis (apt-get, git clone, install.sh), dan wordt dat gemeld via `status_push.py` naar de branch **`status`** (bestand `status.md`, inclusief bootstrap- en cloud-init-log) én automatisch opnieuw geprobeerd bij de volgende tick — zonder dat iemand hoeft in te loggen op de server.
4. Zodra de bot draait, zorgt `update.sh` (aangeroepen via dezelfde tick) voor nieuwe code van `main` en herstart de service bij wijziging of bij een crash.

Alle parameters staan in `config.py` en zijn via `.env` te overschrijven.

## Status volgen

- `status.md` op branch `status`: tijdstip, service-status, code-versie, health, laatste rapport, bot-log, bootstrap-log, cloud-init-log. Geheimen (tokens, keys) worden er altijd uitgefilterd voordat iets naar GitHub gaat.
- `report.json` op dezelfde branch: het laatste dagrapport, alleen gepusht als het is veranderd.

## Bekende benaderingen (zie bouwplan §2 en §8)

- "Final stretch" en "pro traders" zijn Axiom-labels zonder publieke definitie → benaderd.
- Community-check op X wordt niet gemeten; X-link-aanwezigheid en unieke kopers worden gelogd.
- Schaduwfills zijn een bovengrens: mislukte transacties en MEV zitten er niet in.
