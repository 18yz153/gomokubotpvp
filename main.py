import discord
import os

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(m):
  if m.author == client.user:
    return
  if m.content.startswith('inters'):
    await m.channel.send('sb')

client.run(TOKEN)