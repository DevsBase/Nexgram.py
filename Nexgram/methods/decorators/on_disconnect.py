import asyncio

class OnDisconnect:
  def on_disconnect(self):
    def decorator(func):
      self.on_disconnect_listeners[func] = {}
      return decorator
    return decorator
  async def trigger_disconnect(self):
    for mano in self.on_disconnect_listeners:
      asyncio.create_task(mano(self))