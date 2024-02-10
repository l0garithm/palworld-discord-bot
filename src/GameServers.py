from rcon.source import Client

class GameServer:
    def __init__(self, ip: str, port: int, password: str):
        self.host = ip
        self.port = port
        self.password = password

    def run(self, command):
        with Client(self.host, self.port, self.password) as client:
            response = client.run(command)