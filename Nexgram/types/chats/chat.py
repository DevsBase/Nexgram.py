import json

class Chat:
  def __init__(
    self,
    id: int,
    title: str,
    type: str = None,
    username: str = None,
  ):
    self.id = id
    self.title = title
    self.type = type
    if username: self.username = username
  
  def __repr__(self):
    return json.dumps(self.__dict__, indent=2, ensure_ascii=False)