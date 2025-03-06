from aiohttp import web

class Webhook:
  async def __takeCareWebhook(self, request):
    data = request.json()
    self.log.info(f"Got webhook: {data}")
    return web.json_response({"status": "ok"})
  async def createWebhook(self):
    if not self.connected:
      raise ConnectionError("Client is not connected. please start the client.")
    self.webhook = True
    app = web.Application()
    app.router.add_post("/webhook", self.__takeCareWebhook)
    runner = web.AppRunner(app)
    self.log.info("Success. now listening updates from webhook.")
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", self.webhook_port)
    await site.start()