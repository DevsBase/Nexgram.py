from Nexgram.types import User

class GetChatMember:
  async def get_chat_member(self, chat_id: int, user_id: int):
    api, log, url = self.api, self.log, self.ApiUrl
    d = {"chat_id": chat_id, "user_id": user_id}
    r = await api.post(url+"getChatMember", d)
    if r.get('ok') and r.get('result'):
      user = r['result']['user']
      return User(
        client=self,
        id=user.get('id'),
        first_name=user.get('first_name'),
        last_name=user.get('last_name'),
        username=user.get('username'),
        is_bot=user.get('is_bot'),
      )
    return False