import json
import subprocess
import sys
import os

cases = []
with open(sys.argv[1]) as f:
    for l in f.readlines():
        if l:
            cases.append(json.loads(l))

case = cases[int(sys.argv[2])]
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