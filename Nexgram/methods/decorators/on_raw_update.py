class OnRawUpdate:
  def on_raw_update(self):
    def decorator(func):
      self.on_raw_update_listeners[func] = {}
      return func
    return decorator