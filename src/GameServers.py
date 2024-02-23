from rcon.source import Client
from asyncio import sleep as asyncSleep

class GameServer:
    def __init__(self, name: str, host: str, port: int, password: str, guild: str):
        self.name = name
        self.host = host
        self.port = port
        self.password = password
        self.guild = guild

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