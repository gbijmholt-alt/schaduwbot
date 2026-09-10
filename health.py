"""HTTP /health voor UptimeRobot en voor mij: leeftijd laatste event, tellers, open posities."""
import json, time
from aiohttp import web

class Health:
    def __init__(self, port):
        self.port = port; self.last_event = 0.0; self.stats = {}; self.started = time.time()
    async def handle(self, req):
        age = time.time() - self.last_event if self.last_event else None
        body = {"ok": age is not None and age < 120, "last_event_age_s": None if age is None else round(age, 1),
                "uptime_s": round(time.time() - self.started), **self.stats}
        return web.Response(text=json.dumps(body), content_type="application/json", status=200 if body["ok"] else 503)
    async def latest(self, req):
        try: return web.Response(text=open("reports/latest.md").read(), content_type="text/plain")
        except FileNotFoundError: return web.Response(text="nog geen rapport", status=404)
    async def start(self):
        app = web.Application(); app.router.add_get("/health", self.handle); app.router.add_get("/latest", self.latest)
        runner = web.AppRunner(app); await runner.setup()
        await web.TCPSite(runner, "0.0.0.0", self.port).start()
