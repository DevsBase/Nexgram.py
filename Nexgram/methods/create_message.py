from Nexgram.types import User, Chat

class CreateMessage:
  async def create_message(self, data):
    frm = data.get('from_user') or data.get('from')
    ch = data.get('chat')
    forward_from = data.get('forward_from')
    forward_from_chat = data.get("forward_from_chat")
    if frm:
      from_user = User(
        client=self,
        id=frm.get('id'),
        first_name=frm.get('first_name'),
        last_name=frm.get('last_name'),
        username=frm.get('username'),
        is_bot=frm.get('is_bot'),
      )  
    if ch:
      chat = Chat(
        id=ch.get('id'),
        title=ch.get('title'),
        first_name=ch.get('first_name'),
        last_name=ch.get('last_name'),
        type=ch.get('type'),
        username=ch.get('username'),
      )
    if forward_from:
      forward_from = User(
        client=self,
        id=forward_from.get('id'),
        first_name=forward_from.get('first_name'),
        last_name=forward_from.get('last_name'),
        username=forward_from.get("username"),
        is_bot=forward_from.get("is_bot")
      )
    if forward_from_chat:
      forward_from_chat = Chat(
        id=forward_from_chat.get('id'),
        title=forward_from_chat.get('title'),
        first_name=forward_from_chat.get('first_name'),
        last_name=forward_from_chat.get('last_name'),
        type=forward_from_chat.get('type'),
        username=forward_from_chat.get('username'),
      )
    return Message(
      client=self,
      id=data.get('message_id'),
      from_user=from_user,
      chat=chat,
      reply_to_message=None,
      forward_from=forward_from,
      forward_from_chat=forward_from_chat,
      data=data.get('data'),
      caption=data.get('caption'),
      text=data.get('text')
    )