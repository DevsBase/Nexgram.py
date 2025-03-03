import asyncio
import inspect

class Call:
  async def call(self, source, func, *args):
    data = source.get(func)
    tasks = []
    if data.get('filters'):
      for filter_func in list(data.get('filters')):
        if inspect.iscoroutinefunction(filter_func):
          c = await filter_func(*args)
        else:
          c = await asyncio.to_thread(filter_func, *args)
        tasks.append(c)
      if all(tasks):
        self.log.info(f"Line 16 call.py All={all(tasks)}\nTask={tasks}\nData={data}")
        return await func(*args)
    else:
      return await func(*args)