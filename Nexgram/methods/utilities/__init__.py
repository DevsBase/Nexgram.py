from .dispatch_update import Dispatch
from .call import Call
from .create_message import CreateMessage
from .stop import Stop

class Utilities(
  Dispatch,
  Call,
  CreateMessage,
  Stop
):
  pass