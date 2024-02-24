from rcon.source import Client
from asyncio import sleep as asyncSleep
import subprocess

class GameServer:
    def __init__(self, name: str, host: str, port: int, password: str, guild: str, ssh_user: str, ssh_pass: str):
        self.name = name
        self.host = host
        self.port = port
        self.password = password
        self.guild = guild
        self.ssh_user = ssh_user
        self.ssh_pass = ssh_pass

    def run(self, command):
        with Client(self.host, int(self.port), timeout=3.5, passwd=self.password) as client:
            response = client.run(command)
            return response
        
    def showPlayers(self):
        players = self.run('showplayers')
        print(players)
        return(players)
    
    def broadcast(self, message):
        self.run(f'broadcast {message}')
        print(message)

    async def emergency_broadcast(self, message):
        with Client(self.host, int(self.port), timeout=3.5, passwd=self.password) as client:
            for x in range(10):
                client.run(f'broadcast !!!!!!!{message}!!!!!!!')
                await asyncSleep(5)

    async def reboot(self):
        await self.emergency_broadcast("REBOOTING_SERVER")
        with Client(self.host, int(self.port), timeout=3.5, passwd=self.password) as client:
            print("INSERT CODE HERE")