import json

class User:
  def __init__(
    self,
    id: int,
    first_name: str,
    last_name: str = None,
    username: str = None,
  ):
    self.id = id
    self.first_name = first_name
    if last_name: self.last_name = last_name
    if username: self.username = username
  
  def __str__(self):
    return json.dumps(self.__dict__, indent=2)
    
  def __repr__(self):
    return json.dumps(self.__dict__, indent=2)