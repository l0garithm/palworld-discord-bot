from rcon.source import Client

class GameServer:
    def __init__(self, host: str, port: int, password: str, guild: str):
        self.host = host
        self.port = port
        self.password = password
        self.guild = guild

    def run(self, command):
        with Client(self.host, self.port, self.password) as client:
            response = client.run(command)
            return response
        
    def showPlayers(self):
        players = self.run('showplayers')
        print(players)