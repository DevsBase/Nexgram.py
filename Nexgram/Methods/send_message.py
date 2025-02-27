import aiohttp
from Nexgram.errors import BadRequest

class sendMessage:
  async def send_message(self, chat_id, text, reply_to_message_id: int = None, parse_mode=None):
    if not self.connected: raise ConnectionError("Client is not connected, you must connect the client to send message.")
    url = f"https://api.telegram.org/bot{self.bot_token}/sendMessage"
    data = {
      "chat_id": chat_id,
      "text": text,
    }
    if parse_mode: data["parse_mode"] = parse_mode
    if reply_to_message_id: data["reply_to_message_id"] = reply_to_message_id
    async with aiohttp.ClientSession() as x:
      async with x.post(url, json=data) as z:
        z = z.json()
        if not z.get('ok') and z.get('error_code'):
          error_type = z.get('description')
          error = z.get('description').split(':', 1)[1]
          if 'bad request' in error_type.lower():
            raise BadRequest(error)
        return await z.json()