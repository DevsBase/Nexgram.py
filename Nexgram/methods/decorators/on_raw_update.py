class OnRawUpdate:
  def on_raw_update(self, func):
    self.on_raw_update_listeners[func] = True