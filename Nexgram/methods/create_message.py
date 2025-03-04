from Nexgram.types import User

user_args = ['id', 'first_name', 'last_name', 'username', 'is_bot']

class CreateMessage:
  async def create_message(self, data):
    frm = data.get('from_user') or data.get('from')
    if frm:
      output = {'client': self}
      output.update({k: v for k, v in frm.items() if k in user_args})  
      from_user = User(**output)  
      return from_user