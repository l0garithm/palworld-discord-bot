from typing import List
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
    tree.copy_global_to(guild=MY_GUILD)
    await tree.sync(guild=MY_GUILD)
    #await tree.sync()

# Role Command allows for setting the role that can use the bot
@tree.command(name="set_role")
@app_commands.checks.has_permissions(administrator=True)
async def role(interaction: discord.Interaction, role: discord.Role):
    Database.update_guild(interaction.guild_id, role)

    await interaction.response.send_message(f'Setting {role} as the only role that can interact with me')
    required_role = role

# Add a server to current guild
@tree.command(name="add_server")
async def new_server(interaction: discord.Interaction, name: str, ip: str, port: int, pw: str, ssh_user: str, ssh_pass: str):
    await interaction.response.send_message(content="Adding Server with given params", ephemeral=True)
    Database.insert_server(name, ip, port, pw, interaction.guild_id, ssh_user, ssh_pass)

@tree.command(name="list_servers")
async def list_servers(interaction: discord.Interaction):
    await interaction.response.send_message(content=f'Servers: {Database.get_guild_servers(interaction.guild_id)}')

async def server_autocomplete(
        interaction: discord.Interaction, 
        current: str,
        ) -> List[app_commands.Choice[str]]:
        servers = Database.get_guild_server_names(interaction.guild_id)
        # print(servers)
        return [
             app_commands.Choice(name=server[0], value=server[0])
             for server in servers #if current.lower() in server.lower
        ]

@tree.command(name="show_players")
@app_commands.autocomplete(servers=server_autocomplete)
async def show_players(interaction: discord.Interaction, servers: str):
    server = GameServer(*Database.get_server(interaction.guild_id, servers))

    await interaction.response.send_message(content=f'Server Players: {server.showPlayers()}')

@tree.command(name="broadcast")
@app_commands.autocomplete(server=server_autocomplete)
async def broadcast(interaction: discord.Interaction, server: str, message: str):
    broadcast_server = GameServer(*Database.get_server(interaction.guild_id, server))
    broadcast_server.broadcast(message)
    await interaction.response.send_message(content=f'Broadcasted: {message}')
    print("Broadcasted")

@tree.command(name="emergency_broadcast")
@app_commands.autocomplete(server=server_autocomplete)
async def emergency_broadcast(interaction: discord.Interaction, server: str, message: str):
    broadcast_server = GameServer(*Database.get_server(interaction.guild_id, server))
    await interaction.response.defer(thinking=False)
    await broadcast_server.emergency_broadcast(message)
    await interaction.followup.send(content=f'Emergency Broadcasted: {message}')
    print("Broadcasted") 

@tree.command(name="reboot_server")
@app_commands.autocomplete(server=server_autocomplete)
async def reboot_server(interaction: discord.Interaction, server: str):
    shutdownServer = GameServer(*Database.get_server(interaction.guild_id, server))
    await interaction.response.send_message(content=f'Notifying Server Shutdown...')
    await shutdownServer.reboot()
    # await interaction.response.send(content=f'Reboot Successfully Triggered')
    
client.run(Secrets.DISCORD_TOKEN)