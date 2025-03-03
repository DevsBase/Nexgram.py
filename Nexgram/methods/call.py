import asyncio
import inspect

class Call:
  async def call(self, source, func, *args):
    data = source.get(func)
    tasks = []
    if data.get('filters'):
      for filter_func in data.get('filters'):
        if inspect.iscoroutinefunction(z):
          tasks.append(filter_func(*args))
        else:
          tasks.append(asyncio.to_thread(filter_func, *args))
      fk = await asyncio.gather(*tasks)
      if all(fk):
        return await func(*args)
    else:
      return await func(*args)