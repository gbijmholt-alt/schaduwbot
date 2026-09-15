#!/bin/bash
# Aangeroepen door tick.sh (elke 5 minuten): nieuwe code van GitHub ophalen en de bot zo nodig herstellen.
cd /opt/schaduwbot || exit 1
echo "--- update $(date -u +%FT%TZ)"
git fetch -q origin main || { echo "git fetch mislukt"; exit 0; }
if [ "$(git rev-parse HEAD)" != "$(git rev-parse origin/main)" ]; then
  echo "nieuwe code: $(git rev-parse --short origin/main)"
  # Alleen herstarten als er iets verandert dat de bot zelf gebruikt. Wijzigingen in analyses, documentatie of
  # volg_wallets.txt vragen geen herstart (elke herstart geeft een gat in de data van lopende tokens).
  # pumpswap.py staat op deze lijst zolang er geen bruikbare AMM-layout is: de bot importeert het
  # alleen voor de decoder, en die doet niets tot load_layout() iets teruggeeft. Gaat de ingestie
  # ooit aan, dan moet er één keer bewust herstart worden (systemctl restart schaduwbot).
  CHANGED=$(git diff --name-only HEAD origin/main)
  git reset -q --hard origin/main
  cp /opt/schaduwbot.env /opt/schaduwbot/.env 2>/dev/null || echo "waarschuwing: /opt/schaduwbot.env ontbreekt"
  # Herstarten alleen als een bestand verandert dat de bot zélf gebruikt. Dat is een vaste lijst; alles wat
  # er niet op staat (analyses, documentatie, nieuwe analysebestanden) vraagt nooit een herstart. Voorheen was
  # dit een lijst van uitzonderingen, en dan gaf elk níeuw analysebestand een herstart en dus een datagat.
  # pumpswap.py staat er bewust niet op: de bot importeert het alleen voor de decoder, en die doet niets
  # zolang load_layout() niets teruggeeft. Gaat de AMM-ingestie ooit aan: één keer bewust
  # `systemctl restart schaduwbot`.
  BOT_FILES='^(main\.py|store\.py|state\.py|rpc\.py|prices\.py|screening\.py|simulator\.py|health\.py|curve\.py|decoder\.py|config\.py|rpc_endpoint\.txt|report\.py|install\.sh|schaduwbot\.service|bootstrap\.sh|requirements\.txt)$'
  if echo "$CHANGED" | grep -qE "$BOT_FILES"; then
    echo "botcode gewijzigd: herstart"; bash install.sh
  else
    echo "alleen analyses/documentatie gewijzigd: geen herstart"
  fi
elif ! systemctl is-active --quiet schaduwbot; then
  echo "bot draait niet: herstel"
  bash install.sh
fi

# IJking van de poolkoers: klein en vaak. De tweeuurs-analyse levert nooit een meting van minder dan
# 40 minuten na de migratie, en juist die is nodig — daarna is elk koersverschil gewoon koers. Dit
# prijst per tick maximaal 6 tokens die net gemigreerd zijn; een paar RPC-calls, geen herstart.
# Niet tegelijk met de grote analyse draaien: die schrijft in dezelfde database en dan struikelt
# de ijking op "database is locked".
if [ -f /opt/schaduwbot/pumpswap.py ] && ! systemctl is-active --quiet schaduwbot-ijk \
   && ! systemctl is-active --quiet schaduwbot-wallets; then
  systemctl reset-failed schaduwbot-ijk 2>/dev/null
  systemd-run --unit=schaduwbot-ijk --collect -p RuntimeMaxSec=240 /bin/bash -c \
    'cd /opt/schaduwbot && set -a && . ./.env && set +a && nice -n 19 .venv/bin/python pumpswap.py ijk >> reports/ijk.log 2>&1' \
    >/dev/null 2>&1 || echo "ijk starten mislukt"
fi

# Analyses (wallet-analyse, geldstroom, videostrategie): als eigen systemd-taak met lage prioriteit, elke 2 uur,
# en direct opnieuw zodra een van de scripts verandert. Ze lezen de bot-database alleen; de geldstroom en de
# videotoets schrijven naar een eigen database (data/ledger.sqlite) en rekenen alleen nieuwe trades en tokens door.
STAMP=/opt/schaduwbot/reports/.wallets_stamp
# Afrondingsfase: alleen wat de twee lopende toetsen nodig heeft.
#   vamp.py         leest uitsluitend de bot-database (tokens + trades) — hangt van niets af.
#   video_replay.py bevat H2, H3 en H4, en gebruikt de ledger-database alleen voor zijn eigen
#                   replay-cache, niet voor de uitvoer van ledger.py.
# Daarmee kunnen ledger.py, hypotheses.py, pumpswap.py, lotgevallen.py en wallet_analysis.py uit de
# cyclus: hun uitkomsten liggen vast (S1 gezakt, kopieren verliest, afloop gemeten) of staan stil op
# een onopgelost punt (de poolkoers). De snelle ijking van vijf minuten blijft wél draaien, die kost
# bijna niets. Terugzetten = de bestandsnamen hieronder weer toevoegen.
ANALYSES="/opt/schaduwbot/vamp.py /opt/schaduwbot/video_replay.py"
SUM=$(cat $ANALYSES 2>/dev/null | sha1sum | cut -c1-12)
mkdir -p /opt/schaduwbot/reports
if [ -f /opt/schaduwbot/wallet_analysis.py ] && ! systemctl is-active --quiet schaduwbot-wallets; then
  LAST_SUM=$(cat "$STAMP" 2>/dev/null)
  AGE=$(( $(date +%s) - $(stat -c %Y "$STAMP" 2>/dev/null || echo 0) ))
  # De korte keten duurt nog een minuut of tien, dus elk uur in plaats van elke twee uur: dubbel zo
  # snel zicht op H4 en vamp zonder de bak zwaarder te belasten.
  if [ "$LAST_SUM" != "$SUM" ] || [ "$AGE" -gt 3600 ]; then
    systemctl reset-failed schaduwbot-wallets 2>/dev/null
    # Grenzen aan de analyses, om twee redenen. Geheugen: op 15 sept liep de bak naar 2,4 van de
    # 3,8 GB en stond een ronde 50 minuten stil zonder één logregel — vermoedelijk swappen. De bot
    # zelf mag daar nooit onder lijden, want die verzamelt de data en dat is het enige wat niet in
    # te halen is. MemoryHigh remt af (reclaim), MemoryMax doodt pas daarna. Tijd: 90 minuten is te
    # lang om op een vastgelopen ronde te wachten als er elke twee uur een nieuwe komt.
    if systemd-run --unit=schaduwbot-wallets --collect \
         -p MemoryHigh=1200M -p MemoryMax=2200M -p RuntimeMaxSec=3600 /bin/bash -c \
         'cd /opt/schaduwbot && set -a && . ./.env && set +a && for s in '"$ANALYSES"'; do
             if [ ! -f "$s" ]; then echo "OVERGESLAGEN: $s staat er niet" >> reports/wallets.log; continue; fi
             # De walletanalyse is de zwaarste stap (11 minuten, en hij laadt 130.000 tokens in het
             # geheugen) en zijn uitkomst ligt vast: kopieren van slimme wallets verliest. Zolang de
             # keten binnen twee uur moet passen, duwt hij de toetsen die nog wél lopen naar achteren
             # en blokkeert hij de ijking, die niet draait terwijl de analyses bezig zijn. Daarom nog
             # maar eens per twaalf uur.
             if [ "$s" = "wallet_analysis.py" ]; then
               W=reports/.wallets_vol_stamp
               if [ $(( $(date +%s) - $(stat -c %Y "$W" 2>/dev/null || echo 0) )) -lt 43200 ]; then
                 echo "OVERGESLAGEN: $s (minder dan 12 uur geleden gedraaid)" >> reports/wallets.log
                 continue
               fi
               touch "$W"
             fi
             # ionice -c3 is de klasse "idle": het proces krijgt de schijf pas als niemand anders
             # hem wil. De bot schrijft continu, dus een analyse die 7,3 miljoen rijen moet
             # doorlopen komt daar nooit doorheen — op 15 sept stond vamp.py een kwartier stil
             # zonder één regel. Klasse 2 niveau 7 is nog steeds de laagste normale prioriteit,
             # maar wordt niet uitgehongerd.
             echo "--- $s $(date -u +%H:%M:%S)" >> reports/wallets.log
             nice -n 19 ionice -c2 -n7 .venv/bin/python "$s" >> reports/wallets.log 2>&1
           done'; then
      echo "$SUM" > "$STAMP"; echo "analyses gestart ($SUM)"
    else
      echo "analyses starten mislukt"
    fi
  fi
fi
