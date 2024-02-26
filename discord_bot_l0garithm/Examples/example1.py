# Example from discordpy documentation discordpy.readthedocs.io

import discord
import secretsAccess as secrets

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}')
    
    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')


intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)

#old token
client.run('MTIwNDY0NDQ2NjA5OTc1NzA5OA.Ga-uBE.tdB-Oufmkt5WdaaqihCUu2s0I7ARATRK0Tcx90')