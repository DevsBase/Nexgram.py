class OnRawUpdate:
  def on_raw_update(self):
    def decorator(func):
      self.on_raw_update_listeners[func] = True
      return func
    return decorator