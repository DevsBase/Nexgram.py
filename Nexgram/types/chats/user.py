import json

class User:
  def __init__(
    self,
    client: "Nexgram.Client" = None,
    id: int = 0,
    first_name: str = None,
    last_name: str = None,
    username: str = None,
    is_bot: bool = False,
    is_self: bool = False,
  ):
    from Nexgram import Client
    self._ = "Nexgram.types.User"
    self.id = int(id)
    if client:
      self.is_self = is_self or client.me.id == self.id
      if not isinstance(client, Client):
        raise TypeError("You should only pass 'Nexgram.Client' object in 'client' argument not others!")
      self.client = client
    else: self.is_self = is_self
    self.is_bot = is_bot
    self.first_name = first_name
    if last_name: self.last_name = last_name
    if username: self.username = username
      
  def __repr__(self):
    return json.dumps(self.__dict__, indent=2, ensure_ascii=False)