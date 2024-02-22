from typing import List
import discord
from .GameServers import GameServer
from .Player import Player
from . import Database

ATTACHED_GUILDS = []
# ATTACHED_GUILDS = {}

def checkGuildExists(checkGuild):
    guildExists = Database.get_guild(checkGuild)
    if guildExists is not None:
        return True
    else:
        return False
    
def getGuild(guildID):
    row = Database.pull_guild(guildID)
    guild = Guild(*row)
    return guild
    print(guild)

def deleteGuild(guildID):
    Database.delete_guild(guildID)

class Guild():
    def __init__(self, id, name: str, role: str = ''):
        self.guild = id
        self.name = name
        self.required_role = role
        # self.servers = servers
        # self.players = players