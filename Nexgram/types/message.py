import json
from Nexgram.errors import *
from Nexgram import Client

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
    if not isinstance(from_user, User): raise InvalidObject("You should pass 'Nexgram.types.User' object in 'from_user' argument not others.")
    if not isinstance(chat, Chat): raise InvalidObject("You should pass 'Nexgram.types.Chat' object in 'chat' argument not others.")
    if not isinstance(client, Client): raise InvalidObject("You should pass 'Nexgram.Client' object in 'client' argument not others")
    
    self.id = id
    self.from_user = from_user
    self.chat = chat
    self.text = text
    self.client = client
  
  def __repr__(self):
    return json.dumps(self.__dict__, indent=2, ensure_ascii=False, default=lambda o: json.loads(repr(o)))
  
  async def reply(self, text: str, parse_mode: str = None):
    client = self.client
    if not client.connected: raise ConnectionError("Client is not connected, you must connect the client to send message.")
    await client.send_message(
      chat_id=self.chat.id,
      text=text,
      parse_mode=parse_mode,
    )