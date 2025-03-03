import asyncio
import inspect

class Call:
  async def call(self, source, func, *args):
    data = source.get(func)
    tasks = []
    if data.get('filters'):
      for filter_func in list(data.get('filters')):
        if inspect.iscoroutinefunction(filter_func):
          tasks.append(filter_func(*args))
        else:
          tasks.append(asyncio.to_thread(filter_func, *args))
      fk = await asyncio.gather(*tasks)
      if all(fk):
        self.log.info(f"Line 16 call.py All={all(tasks)}\nTask={tasks}\nData={data}\nfk={fk}")
        return await func(*args)
    else:
      return await func(*args)