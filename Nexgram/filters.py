import logging
import inspect
import asyncio
from Nexgram.types import Message

log = logging.getLogger(__name__)

class Filter:
  def __init__(self, func):
    self.func = func
    self.is_async = inspect.iscoroutinefunction(func)
  async def __call__(self, *args, **kwargs):
    if self.is_async:
      return await self.func(*args, **kwargs)
    return self.func(*args, **kwargs)
  def __and__(self, other):
    async def combined(*args, **kwargs):
      r1 = await self(*args, **kwargs) if self.is_async else self(*args, **kwargs)
      r2 = await other(*args, **kwargs) if other.is_async else other(*args, **kwargs)
      return r1 and r2
    return Filter(combined)
  def __or__(self, other):
    async def combined(*args, **kwargs):
      r1 = await self(*args, **kwargs) if self.is_async else self(*args, **kwargs)
      r2 = await other(*args, **kwargs) if other.is_async else other(*args, **kwargs)
      return r1 or r2
    return Filter(combined)
  def __invert__(self):
    async def inverted(*args, **kwargs):
      r1 = await self(*args, **kwargs) if self.is_async else self(*args, **kwargs)
      return not r1
    return Filter(inverted)
    
def create(func):
  if isinstance(func, Filter):
    return func
  name = getattr(func, "__name__", "CustomFilter")
  return type(name, (Filter,), {"__call__": func})(func)
     
text = create(lambda _, message: message.text)

def command(cmd, prefix=['/']):
  async def wrapper(_, __, message):
    if not isinstance(message, Message): return
    if message.text:
      for x in prefix:
        return str(message.text).lower().startswith(x+cmd.lower())
  return create(wrapper)
  
urls = ["http://t.me/", "https://t.me/", "www.t.me/", "@", "http://telegram.dog/", "https://telegram.dog/"]
  
def user(id):
  async def wrapper(_, __, m):
    src = m.from_user
    if isinstance(id, (int, str)) and str(id).isdigit():
      return src.id == int(id)
    elif isinstance(id, list):
      for x in id:
        if isinstance(x, (int, str)) and str(x).isdigit():
          return src.id == int(x)
        else:
          return any(x.replace(z, "").lower() == src.username.lower() for z in urls)      
    return any(id.replace(x, "").lower() == src.username.lower() for x in urls)
  return create(wrapper)
  
def chat(id):
  async def wrapper(_, __, m):
    src = m.chat
    if isinstance(id, (int, str)) and str(id).isdigit():
      return src.id == int(id)
    elif isinstance(id, list):
      for x in id:
        if isinstance(x, (int, str)) and str(x).isdigit():
          return src.id == int(x)
        else:
          return any(x.replace(z, "").lower() == src.username.lower() for z in urls)      
    return any(id.replace(x, "").lower() == src.username.lower() for x in urls)
  return create(wrapper)