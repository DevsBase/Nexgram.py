from .on_disconnect import OnDisconnect
from .on_raw_update import OnRawUpdate
from .on_message import OnMessage
from .on_callback_query import OnCallbackQuery
from .on_inline_query import OnInlineQuery

class Decorators(
  OnRawUpdate,
  OnDisconnect,
  OnMessage,
  OnCallbackQuery,
  OnInlineQuery,
):
  pass