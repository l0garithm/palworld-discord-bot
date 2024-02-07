# Example "A Minimal Bot" by discordpy.readthedocs.io

import discord

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

client.run('MTIwNDY0NDQ2NjA5OTc1NzA5OA.Ga-uBE.tdB-Oufmkt5WdaaqihCUu2s0I7ARATRK0Tcx90')