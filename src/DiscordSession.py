import discord
from discord import app_commands
from ..src import Secrets
from .Guilds import Guild
from . import Guilds
from .GameServers import GameServer
from . import Database
from .MyCommandTree import MyCommandTree

token = Secrets.DISCORD_TOKEN
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
#tree = app_commands.CommandTree(client)
# UNCOMMENT TO USE MyCommandTree
tree = MyCommandTree(client)
required_role: discord.Role

MY_GUILD = discord.Object(id=Secrets.DISCORD_GUILD_ID)
client_guilds = []

@client.event
async def on_guild_join(guild):
    Database.insert_guild(guild.id, guild.name)
    await tree.sync()

@client.event
async def on_guild_remove(guild):
    Database.delete_guild(guild.id)


# ON READY: When Startup Complete
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    Database.createTables()

    await tree.sync()

# Role Command allows for setting the role that can use the bot
@tree.command(name="set_role")
@app_commands.checks.has_permissions(administrator=True)
async def role(interaction: discord.Interaction, role: discord.Role):
    Database.update_guild(interaction.guild_id, role)

    await interaction.response.send_message(f'Setting {role} as the only role that can interact with me')
    required_role = role

# Add a server to current guild
@tree.command(name="add_server")
async def new_server(interaction: discord.Interaction, name: str, ip: str, port: int, pw: str):
    await interaction.response.send_message(content="Adding Server with given params", ephemeral=True)
    Database.insert_server(name, ip, port, pw, interaction.guild_id)

@tree.command(name="list_servers")
async def get_roles(interaction: discord.Interaction):
    await interaction.response.send_message(content=f'Servers: {Database.get_guild_servers(interaction.guild_id)}')

client.run(Secrets.DISCORD_TOKEN)