class BadRequest(Exception):
  def __init__(self, message="Bad Request"):
    super().__init__(message)