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
     
def text_filter(_, __, message):
  if not isinstance(message, Message): 
    return False
  return message.text

text = create(text_filter)

def command(cmd, prefix=['/']):
  async def wrapper(_, __, m):
    if not isinstance(m, Message):
      return False
    p = next((p for p in prefix if m.text.startswith(p)), None)
    return p and (m.text[len(p):] in cmd if isinstance(cmd, list) else m.text[len(p):] == cmd)
  return create(wrapper)
  
def check(val, id1, id2):
  val = int(val) if isinstance(val, (int, str)) and str(val).lstrip('-').isdigit() else val
  return val == id1 or val == id2

def user(ids_list):
  async def wrapper(_, __, m):
    ids = [ids_list] if not isinstance(ids_list, list) else ids_list
    urls = ["http://t.me/", "https://t.me/", "www.t.me/", "@", "http://telegram.dog/", "https://telegram.dog/"]
    return any(check(i, m.from_user.id, (m.from_user.username or "").lower()) or 
               any(i.replace(x, "").lower() == (m.from_user.username or "").lower() for x in urls)
               for i in ids)
  return create(wrapper)

def chat(ids_list):
  async def wrapper(_, __, m):
    ids = [ids_list] if not isinstance(ids_list, list) else ids_list
    urls = ["http://t.me/", "https://t.me/", "www.t.me/", "@", "http://telegram.dog/", "https://telegram.dog/"]
    return any(check(c, m.chat.id, (m.chat.username or "").lower()) or 
               any(c.replace(x, "").lower() == (m.chat.username or "").lower() for x in urls)
               for c in ids)
  return create(wrapper)