from Nexgram.errors import *
from Nexgram.types import *
import asyncio

class Dispatch:
  async def __dispatch_helper(self, src, update, type='message'):
    try:
      m = update.get(type)
      message = await self.create_message(m)
      for x in src:
        asyncio.create_task(self.call(src, x, self, message))
    except Exception as e:
      log.error(f"[DispatchUpdate] Line 13: {e}, message: {m}")
  
  async def dispatch_update(self, update):
    log = self.log
    for gf in self.on_listeners:
      asyncio.create_task(gf(update))
    if update.get('message'):
      type, src = "message", 
      await self.__dispatch_helper(src=src,update=update,type=type)
    elif update.get("callback_query"):
      type, src = "callback_query", self.on_callback_query_listeners
      await self.__dispatch_helper(src=src,update=update,type=type)
    elif update.get("inline_query"):
      type, src = "inline_query", self.on_inline_query_listeners
      await self.__dispatch_helper(src=src,update=update,type=type)