import logging
import httpx
import aiohttp
import asyncio
from .methods import *
from .errors import *
from .types import *
from .api import Api

log = logging.getLogger(__name__)

class Client(Methods):
  def __init__(
    self,
    name: str,
    bot_token: str,
  ):
    self.name = name
    self.bot_token = bot_token
    self.connected = False
    self.me = None
    self.offset = 0
    self.polling = False
    self.ApiUrl = f"https://api.telegram.org/bot{self.bot_token}/"
    self.api = Api()
    self.log = log
    # Decorators --
    self.on_message_listeners = []
    self.on_disconnect_listeners = {}
    self.on_listeners = {}
    
  async def start(self, start_polling=False):
    url = f"https://api.telegram.org/bot{self.bot_token}/getMe"
    async with aiohttp.ClientSession() as session:
      async with session.get(url) as r:
        r = await r.json()
        if r.get("ok"):
          self.connected = True
          r = r["result"]
          self.me = User(
            r['id'],
            r['first_name'],
            username=r['username'],
            is_self=True,
            is_bot=True,
          )
          log.info(f"Client connected as {self.me.first_name} (@{self.me.username})")
          if start_polling:
            try:
              loop = asyncio.get_running_loop()
            except RuntimeError:
              loop = asyncio.new_event_loop()
              asyncio.set_event_loop(loop)
            loop.create_task(self.start_polling())
            log.info("Exp. Feature Started: Loop created.")
          return self.me
        raise ValueError("Failed to connect with your bot token. Please make sure your bot token is correct.")

  async def start_polling(self):
    if not self.connected:
      raise ConnectionError("Client is not connected. Please connect the client and start polling.")
    elif self.polling: raise PollingAlreadyStartedError("Polling already started, why you trying again and again? didn't you receive any updates?")
    self.polling = True
    log.info("Nexgram polling started!")
    self.first_start = True
    while self.polling:
      try:
        async with aiohttp.ClientSession() as session:
          params = {"offset": self.offset, "timeout": 30}
          async with session.get(f"https://api.telegram.org/bot{self.bot_token}/getUpdates", params=params) as response:
            updates = await response.json()
            if "result" in updates and not self.first_start:
              for update in updates["result"]:
                self.offset = update["update_id"] + 1
                asyncio.create_task(self.dispatch_update(update))
            elif "result" in updates and self.first_start: self.first_start = False
      except Exception as e:
        log.error(f"Error in start_polling: {e}")
  
  async def stop(self):
    await self.trigger_disconnect()
    self.polling = False
    self.connected = False
    log.info("Client stopped.")