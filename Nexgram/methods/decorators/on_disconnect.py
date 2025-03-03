import asyncio

class OnDisconnect:
  def on_disconnect(self, mano):
    self.on_disconnect_listeners[mano] = True
  async def trigger_disconnect(self):
    for mano in self.on_disconnect_listeners:
      asyncio.create_task(mano(self))
    return True