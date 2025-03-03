import json
from .inline_keyboard_button import InlineKeyboardButton

class InlineKeyboardMarkup:
  def __init__(self, inline_keyboard: List[List["types.InlineKeyboardButton"]]):
    self._ = "Nexgram.types.InlineKeyboardMarkup"
    if not isinstance(inline_keyboard, list):
      raise TypeError("Failed to read buttons, you should pass list always!")
    
    for x in inline_keyboard:
      if not isinstance(x, list):
        raise TypeError("Failed to read buttons, you should pass 2 list always!")
      for z in x:
        if not isinstance(z, InlineKeyboardButton):
          raise TypeError("Failed to read buttons, you should always pass 'Nexgram.types.InlineKeyboardButton' object always!")
          
    self.inline_keyboard = inline_keyboard
  def __repr__(self):
    return json.dumps(self.__dict__, indent=2, ensure_ascii=False)