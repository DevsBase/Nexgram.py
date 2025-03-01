"""Api class used to post/get from BotApi, I don't like to create code for calling api each time."""
import aiohttp

class Api:
  async def post(self, url, json: dict = {}):
    async with aiohttp.ClientSession() as mano:
      async with mano.post(url=url, json=data) as ily:
        z = await ily.json()
        return z
  async def get(self, url):
    pass