from .send_message import sendMessage
from .dispatch_update import Dispatch
from .call import Call
from .decorators import Decorators

class Methods(
  sendMessage,
  Dispatch,
  Call,
  Decorators,
):
  pass