from rcon.source import Client
from ..src import Secrets

with Client(Secrets.SERVER_HOST, int(Secrets.SERVER_PORT), timeout=3.5, passwd=Secrets.SERVER_PW) as client:
    response = client.run('showplayers')

print(response)