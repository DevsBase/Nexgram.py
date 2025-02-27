import json
from Nexgram.errors import *

class Message:
  def __init__(
    self,
    client: "Nexgram.Client",
    id: int,
    from_user: "Nexgram.types.User",
    chat: "Nexgram.types.Chat",
    text: str = None,
  ):
    from Nexgram.types import User, Chat
    from Nexgram import Client
    
    if not isinstance(from_user, User): raise InvalidObject("You should pass 'Nexgram.types.User' object in 'from_user' argument not others.")
    if not isinstance(chat, Chat): raise InvalidObject("You should pass 'Nexgram.types.Chat' object in 'chat' argument not others.")
    if not isinstance(client, Client): raise InvalidObject("You should pass 'Nexgram.Client' object in 'client' argument not others")
    
    self.id = id
    self.from_user = from_user
    self.chat = chat
    self.text = text
    self.client = client
  
  def __repr__(self):
    mf = ["client"]
    data = {k: v for k, v in self.__dict__.items() if k not in mf}
    return json.dumps(
      data,
      indent=2,
      ensure_ascii=False,
      default=lambda o: o.__dict__ if hasattr(o, "__dict__") else o
    )
    
  async def reply(self, text: str, parse_mode: str = None):
    client = self.client
    if not client.connected: raise ConnectionError("Client is not connected, you must connect the client to send message.")
    await client.send_message(
      chat_id=self.chat.id,
      text=text,
      reply_to_message_id=self.id,
      parse_mode=parse_mode,
    )