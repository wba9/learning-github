import discord, requests, json

def get_meme():
  response = requests.get('https://meme-api.com/gimme')
  json_data = json.loads(response.text)
  return json_data['url']

class MyClient(discord.Client):
  
  async def on_ready(self):
    print('Logged on as {0}!'.format(self.user))

  async def on_message(self, message):
    if message.author == self.user:
     return

    if message.content.lower().startswith('gimmeme'):
     await message.channel.send(get_meme())

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('MTQwMjkzMDExNjQ4NDM5OTE0NA.Gr3i4P.GcKmuOfZOAnW0LUkdMS1h56OB2BL9J16pTAeXw') 

