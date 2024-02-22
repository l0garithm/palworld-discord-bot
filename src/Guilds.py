from typing import List
import discord
from .GameServers import GameServer
from .Player import Player
from . import Database

ATTACHED_GUILDS = []
# ATTACHED_GUILDS = {}

def checkGuildExists(checkGuild):
    for guild in ATTACHED_GUILDS:
        # print(f'Check ID: {checkGuild}')
        # print(f'Guild ID: {guild.guild}')
        if checkGuild == guild.guild:
            return True
        else:
            return False
    
def appendGuilds(guild):
    ATTACHED_GUILDS.append(Guild(guild.id))

def guildToDict(guildId):
    guild = getGuild(guildId)
    guildDict = {"guild":guild.guild, "required_role":guild.required_role, "players": guild.players, "game_servers": guild.game_servers}
    return guildDict

def addGuild(guildID, name):
    Database.insert_guild(guildID, name)

def getGuild(guildID):
    # for guild in ATTACHED_GUILDS:
    #     if guildID == guild.guild:
    #         print('succses')
    #         return guild
    Database.pull_guild(guildID)

class Guild():
    def __init__(self, id, role: str =None, servers=None, players=None):
        self.guild = id
        # self.name = name
        self.required_role = role
        self.servers = servers
        self.players = players