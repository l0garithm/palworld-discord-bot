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
tree = app_commands.CommandTree(client)
# UNCOMMENT TO USE MyCommandTree
#tree = MyCommandTree(client)
required_role: discord.Role

MY_GUILD = discord.Object(id=Secrets.DISCORD_GUILD_ID)
client_guilds = []

@client.event
async def on_guild_join(guild):
    # newGuild = Guild(guild.id)

    if Guilds.checkGuildExists(guild.id) != True:
        Guilds.appendGuilds(guild.id)
        newGuild = Guilds.guildToDict(guild.id)

        Database.insert(newGuild)


# ON READY: When Startup Complete
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

    # rows = Database.pull_guilds()
    # print(f'Rows {rows}')

    # for row in rows:
    #     # Guilds.ATTACHED_GUILDS[row.pop('guild')] = row
    #     print(*row)
    #     Guilds.ATTACHED_GUILDS.append(Guild(*row))
    # print(Guilds.ATTACHED_GUILDS[0].g)

    # print(f'Guilds: {Guilds.ATTACHED_GUILDS[0].required_role}')
    Guilds.checkGuildExists(MY_GUILD.id)
    tree.copy_global_to(guild=MY_GUILD)
    await tree.sync(guild=MY_GUILD)
    Database.insert_guild('1158872977048342608', 'Home', 'null')

# Role Command allows for setting the role that can use the bot
@tree.command(name="set_role")
@app_commands.checks.has_permissions(administrator=True)
async def role(interaction: discord.Interaction, role: discord.Role):

    # guild = Guilds.getGuild(interaction.guild_id)
    # guild.required_role = role

    # print(f"Setting {role} as the only role that can interact with me in {guild.guild}")
    # Database.update(guild.guild, Database.DB_REQUIRED_ROLE, role)
    Database.update_guild(interaction.guild_id, role)

    await interaction.response.send_message(f'Setting {role} as the only role that can interact with me')
    required_role = role
    # await tree.interaction_check(interaction)

@tree.command(name="add_server")
async def new_server(interaction: discord.Interaction, ip: str, port: int, pw: str):
    await interaction.response.send_message(content="Adding Server with given params", ephemeral=True)
    Database.insert_server(ip, port, pw)




client.run(Secrets.DISCORD_TOKEN)