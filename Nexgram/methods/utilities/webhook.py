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
    self.log.info("Success. now listening updates from webhook.")
    web.run_app(app, host="0.0.0.0", port=self.webhook_port)