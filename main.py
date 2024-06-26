import revolt
import requests
import asyncio
import os
import random
import always_on
import requests
class Client(revolt.Client):
  
  async def on_ready(self):
    print('Run  videoBOT')
    
  async def on_message(self, message: revolt.Message):
    # メッセージが "yd " で始まるかをチェック
     if message.startswith("yd "):
       await message.channel.send("OK-1")
        # "yd "を取り除いた後の部分が文字列として取得されます
        video_id = message[3:]
        # ここでqueryを使って適切な処理を行います
        api_url = f'https://invidious.fdn.fr/api/v1/videos/{video_id}'
        await message.channel.send("OK-2")
        response = requests.get(api_url)
        data = response.json()
        video_url = data['formats'][0]['url']
        channel_id = "01HN0EX161E3JZ7TDY1SRRB2PM"
        await message.channel.send("OK-3")
        await message.channel.send(f"{video_id}")
async def main():
  async with revolt.utils.client_session() as session:
    client = Client(session, os.environ['R'])
    await client.start()
    





always_on.activate()

asyncio.run(main())
