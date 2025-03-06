from aiohttp import web

class Webhook:
  async def takeCareWebhook(self, request):
    data = await request.json()
    self.log.info(f"Got webhook: {data}")
    return web.json_response({"ok": True})
  
  async def createWebhook(self):
    if not self.connected:
      raise ConnectionError("Client is not connected. please start the client.")
    self.webhook, api, url = True, self.api, self.ApiUrl
    um = await api.post(url+"setWebhook", {"url": self.webhook_url+"/webhook"})
    if not um.get('ok'):
      raise Exception(f"Telegram says: {um}")
    app = web.Application()
    app.router.add_post("/webhook", self.takeCareWebhook)
    runner = web.AppRunner(app, access_log=None))
    self.log.info("Success. now listening updates from webhook.")
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", self.webhook_port)
    await site.start()