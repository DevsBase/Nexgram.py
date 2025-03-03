import logging
import inspect

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
      return (await self(*args, **kwargs)) and (await other(*args, **kwargs))
    return Filter(combined)

  def __or__(self, other):
    async def combined(*args, **kwargs):
      return (await self(*args, **kwargs)) or (await other(*args, **kwargs))
    return Filter(combined)

  def __invert__(self):
    async def inverted(*args, **kwargs):
      return not (await self(*args, **kwargs))
    return Filter(inverted)
    
def create(func):
  return type(func.__name__, (Filter,), {})(func)
  
text = create(lambda _, message: message.text)