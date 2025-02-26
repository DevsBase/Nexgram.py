import json
from Nexgram.errors import *

class Message:
  def __init__(
    self,
    id: int,
    from_user: "Nexgram.types.User",
    chat: "Nexgram.types.Chat",
    text: str = None,
  ):
    from Nexgram.types import User, Chat
    if not isinstance(from_user, User): raise InvalidObject("You should pass User object in from_user not others.")
    if not isinstance(chat, Chat): raise InvalidObject("You should pass Chat object in 'chat' not others.")
    self.id = id
    self.from_user = from_user
    self.chat = chat
    self.text = text
  
  def __repr__(self):
    return json.dumps(self.__dict__, indent=2, ensure_ascii=False, default=lambda o: json.loads(repr(o)))