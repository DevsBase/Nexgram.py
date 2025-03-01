class BadRequest(Exception):
  def __init__(self, err):
    super().__init__(err)
  def __str__(self):
    return f"Nexgram.errors.BadRequest: {self.args[0]}"