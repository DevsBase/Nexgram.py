import json

class Message:
  def __init__(
    self,
    id: int,
    from_user: "Nexgram.types.User",
    text: str = None,
  ):
    self.id = id
    self.from_user = from_user
    self.text = text
  
  def __repr__(self):
    return json.dumps(self.__dict__, indent=2, ensure_ascii=False, default=lambda o: json.loads(repr(o)))