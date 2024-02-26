from subprocess import Popen
from subprocess import PIPE
from ..src import Secrets
import pexpect
import time
import sys

_TRUST_HOST = '(yes/no/)'
_PASS_PROMPT = 'password:'
_TERM_INPUT = '\$'

with pexpect.spawn(f'ssh {Secrets.SERVER_USER}@{Secrets.SERVER_HOST}', encoding='utf-8') as proc:
    index = proc.expect([_TRUST_HOST, _PASS_PROMPT, pexpect.EOF, pexpect.TIMEOUT])

    print(index)

    if (index == 0) or (index == 1):
        if(index == 0):
            proc.expect('(yes/no/)')
            proc.sendline('yes')
            proc.expect(_PASS_PROMPT)

        proc.sendline(str(Secrets.SERVER_PASS))
        proc.expect(_TERM_INPUT)
        proc.sendline('echo "hello"')
        proc.expect(_TERM_INPUT)
        print(proc.before)

    elif index == 2 or 3:
        print("Error")