from .send_message import sendMessage
from .dispatch_update import Dispatch
from .decorators import Decorators

class Methods(
  sendMessage,
  Dispatch,
  Decorators,
):
  pass