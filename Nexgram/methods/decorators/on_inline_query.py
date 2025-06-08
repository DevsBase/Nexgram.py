from Nexgram.filters import Filter
from Nexgram import filters as f

class OnInlineQuery:
  def on_inline_query(self, filters=None):      
    def decorator(mano):
      if not isinstance(filters, Filter) and not filters is None:
        filters = f.create(filters)
      self.on_inline_query_listeners[mano] = filters if isinstance(filters, Filter) else None
      return mano
    return decorator