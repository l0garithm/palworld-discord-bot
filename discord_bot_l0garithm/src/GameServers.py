from rcon.source import Client
from asyncio import sleep as asyncSleep
import pexpect  

class GameServer:

    def __init__(self, name: str, host: str, port: int, password: str, guild: str, ssh_user: str, ssh_pass: str):
        self.name = name
        self.host = host
        self.port = port
        self.password = password
        self.guild = guild
        self.ssh_user = ssh_user
        self.ssh_pass = ssh_pass
        self._TRUST_HOST = '(yes/no/)'
        self._PASS_PROMPT = 'password:'
        self._TERM_INPUT = '\$'

    def run(self, command):
        with Client(self.host, int(self.port), timeout=3.5, passwd=self.password) as client:
            response = client.run(command, enforce_id = False)
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
                self.run(f' !!!!!!!{message}!!!!!!!')
                await asyncSleep(5)

    async def reboot(self):
        await self.emergency_broadcast("REBOOTING_SERVER")
        with pexpect.spawn(f'ssh {self.ssh_user}@{self.host}', encoding='utf-8') as proc:
            index = proc.expect([self._TRUST_HOST, self._PASS_PROMPT, pexpect.EOF, pexpect.TIMEOUT])

            print(index)

            if (index == 0) or (index == 1):
                if(index == 0):
                    proc.expect(self._TRUST_HOST)
                    proc.sendline('yes')
                    proc.expect(self._PASS_PROMPT)

                proc.sendline(str(self.ssh_pass))
                proc.expect(self._TERM_INPUT)
                proc.sendline('reboot now')
                proc.expect(self._TERM_INPUT)
                print(proc.before)

            elif index == 2 or 3:
                print("Error")
                
            
            proc.close()