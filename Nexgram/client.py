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
    self.on_listeners = []
    self.offset = 0
    self.polling = False
    self.on_message_listeners = []
    self.ApiUrl = f"https://api.telegram.org/bot{self.bot_token}/"
    self.api = Api()

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
          return self.m
        raise ValueError("Failed to connect with your bot token. Please make sure your bot token is correct.")

  async def start_polling(self):
    if not self.connected:
      raise ConnectionError("Client is not connected. Please connect the client and start polling.")
    elif self.polling: raise PollingAlreadyStartedError("Polling already started, why you trying again and again? didn't you receive any updates?")
    self.polling = True
    log.info("Nexgram polling started!")
    while self.polling:
      try:
        async with aiohttp.ClientSession() as session:
          params = {"offset": self.offset, "timeout": 30}
          async with session.get(f"https://api.telegram.org/bot{self.bot_token}/getUpdates", params=params) as response:
            updates = await response.json()
            if "result" in updates:
              for update in updates["result"]:
                self.offset = update["update_id"] + 1
                asyncio.create_task(self.__dispatch_update(update))
      except Exception as e:
        log.error(f"Error in start_polling: {e}")

  async def __dispatch_update(self, update):
    for x in self.on_listeners:
      asyncio.create_task(x(update))
    if update.get('message'):
      try:
        m = update.get('message')
        frm = m.get('from')
        ch = m.get('chat')
        from_user = User(
          frm['id'],
          frm['first_name'],
          username=frm.get('username'),
          is_bot=frm.get('is_bot'),
          is_self=frm['id'] == self.me.id,
        )
        chat = Chat(
          id=ch['id'],
          title=ch.get('title'),
          first_name=ch.get('first_name'),
          last_name=ch.get('last_name'),
          type=ch.get('type'),
          username=ch.get('username')
        )
        reply_to_message = None
        if m.get('reply_to_message'):
          reply_to_message = Message()
          while True:
            
        message = Message(
          client=self,
          id=m['message_id'],
          from_user=from_user,
          chat=chat,
          reply_to_message=reply_to_message,
          text=m.get('text')
        )
        
        for x in self.on_message_listeners:
          asyncio.create_task(x(self, message))
      except Exception as e:
        log.error(f"Line 68 Nexgram.client: {e}, message: {m}")
  
  def on(self, func):
    self.on_listeners.append(func)
  
  def on_message(self, fk):
    self.on_message_listeners.append(fk)
  
  async def stop(self):
    self.polling = False
    self.connected = False
    log.info("Client stopped.")