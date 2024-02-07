# Example "A Minimal Bot" by discordpy.readthedocs.io

import discord
from ..src import Secrets


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('$hello'):
        await message.channel.send(f'Hello i\'m {client.user}!')

# Old token
client.run(Secrets.Secrets._discord_token)