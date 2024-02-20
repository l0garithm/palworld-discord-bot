from dotenv import dotenv_values
import os


secrets = dotenv_values()
print(secrets)
DISCORD_TOKEN = secrets["DISCORD_TOKEN"]
DISCORD_GUILD = secrets["DISCORD_GUILD"]
DISCORD_GUILD_ID = secrets["DISCORD_GUILD_ID"]

SERVER_HOST = secrets["SERVER_HOST"]
SERVER_PORT = secrets["SERVER_PORT"]
SERVER_PW   = secrets["SERVER_PW"]