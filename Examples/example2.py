# Example "A Minimal Bot" by discordpy.readthedocs.io

from typing import List
import discord
from discord.ext import commands
from discord import app_commands
from ..src import Secrets

intents = discord.Intents.default()
intents.message_content = True

currentActivity = discord.CustomActivity(name="Wienerin")

client = discord.Client(intents=intents, activity=currentActivity)

MY_GUILD = discord.Object(id=Secrets.DISCORD_GUILD_ID)

tree = app_commands.CommandTree(client)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user} in {client.private_channels}')
    tree.copy_global_to(guild=MY_GUILD)
    await tree.sync(guild=MY_GUILD)

@tree.command(name="hello")
async def hello(interaction: discord.Interaction, hello: str):
    print("Hello command called")
    await interaction.response.send_message(f'Hello there {interaction.user}')

@hello.autocomplete('hello')
async def hello_autocomplete(
    interaction: discord.Interaction,
    current: str,
) -> List[app_commands.Choice[str]]:
    hello_options = ['world', 'moto', 'person', 'logan']
    return [
        app_commands.Choice(name=hello, value=hello)
        for hello in hello_options if current.lower() in hello.lower()
    ]

@client.event
async def on_guild_channel_delete(channel):
    print(f'Channel Deleted: {channel} in {channel.guild}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('hello'):
        await message.channel.send(f'Hello i\'m {client.user}!')
        await message.channel.send(f'Here are the commands {tree.get_commands(guild=MY_GUILD)}')

# Old token
client.run(Secrets.DISCORD_TOKEN)