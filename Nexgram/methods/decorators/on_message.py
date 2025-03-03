import asyncio
import inspect
from Nexgram.filters import Filter
from Nexgram import filters as f

class OnMessage:
  def __init__(self):
    self.on_message_listeners = {}  

  def on_message(self, filters):
    if not isinstance(filters, Filter):
      filters = f.create(filters)  

    def decorator(mano):
      if mano in self.on_message_listeners:
        raise Exception("You have already used this same decorator, you cannot use it multiple times!")
      self.on_message_listeners[mano] = filters  
      return mano
    return decorator

  async def trigger(self, *args):
    for func, filter_func in self.on_message_listeners.items():
      if inspect.iscoroutinefunction(filter_func.func):
        passed = await filter_func(*args)  
      else:
        passed = await asyncio.to_thread(filter_func.func, *args)  

      if passed:
        await func(*args)