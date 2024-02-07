from dotenv import dotenv_values
import os

class Secrets:
    secrets = dotenv_values()
    _discord_token = secrets["DISCORD_TOKEN"]

    @staticmethod
    def getDiscordToken():
        print(Secrets.secrets)
        return Secrets._discord_token