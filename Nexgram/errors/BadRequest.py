class BadRequest(Exception):
  def __init__(self, message="Bad Request"):
    super().__init__(message)
  def __str__(self):
    return f"{self.__class__.__name__}: {self.args[0]}"