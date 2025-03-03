from Nexgram.filters import Filter
from Nexgram import filters as f

class OnMessage:
  def on_message(self, filters):
    if not isinstance(filters, Filter):
      filters = f.create(filters)
    def decorator(mano):
      if mano in self.on_message_listeners:
        raise Exception("You have already used this same decorator, you cannot use it multipul times!")
      self.on_message_listeners[mano] = {'filters': filters}
    return decorator