import aiohttp

class sendMessage:
  async def send_message(self, chat_id, text, parse_mode=None):
    if not self.connected: raise ConnectionError("Client is not connected, you must connect the client to send message.")
    url = f"https://api.telegram.org/bot{self.bot_token}/sendMessage"
    data = {
      "chat_id": chat_id,
      "text": text,
    }
    if parse_mode: data["parse_mode"] = parse_mode
    async with aiohttp.ClientSession() as x:
      async with x.post(url, json=data) as z:
        return await z.json()