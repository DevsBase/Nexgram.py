from .send_message import sendMessage
from .dispatch_update import Dispatch
from .decorators import Decorators
from .call import Call
from .forward_messages import ForwardMessages

class Methods(
  sendMessage,
  Dispatch,
  Decorators,
  Call,
  ForwardMessages,
):
  pass