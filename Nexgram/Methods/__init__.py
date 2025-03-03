from .send_message import sendMessage
from .dispatch_update import Dispatch
from .call import Call

class Methods(
  sendMessage,
  Dispatch,
  Call
):
  pass