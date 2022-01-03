import subprocess
import time
import select
import random
import os
import json
from pathlib import Path

seed = time.time()
print(seed)
random.seed(seed)

FOLDER = 'fengshui4'

# define some common size values usable for different inputs
_SIZES = [i for i in range(0,0xff)]
_SIZES += [2**i for i in range(0,15)]
_SIZES += [(2**i)+1 for i in range(0,15)]
_SIZES += [(2**i)-1 for i in range(0,15)]
_SIZES += ([0]*50)

# define some flags from sudo -h
ARG1 = ["-A","-B","-E","-e","-H","-K","-k","-l","-n","-P","-S","-s"]
ARG1 += [None, None, None, None, None, None, None]

# dump a testcase into a logfile
def dump_file(fname, lines, backtrace, arg, env):

    # create the folders if they don't exist
    directory = os.path.dirname(fname)
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    # don't write the dump file if it's already too large
    if os.path.isfile(fname) and Path(fname).stat().st_size > 200000:
        return

    with open(fname, 'a+') as f:
        f.write("----------------------------\n")
        f.write(lines)
        f.write("\nbacktrace:\n")
        f.write("\n".join(backtrace))
        f.write("\n\n")

# this will run sudoedit to check if it crashes
def sudoedit_crash_check(arg,env):
    p = subprocess.Popen(["/usr/bin/stdbuf","-o0","/usr/local/bin/sudoedit"]+arg, 
        env=env, bufsize=0, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    try:
        lines = p.communicate(b"x\nx\nx\nx\n",timeout=0.1)
    except subprocess.TimeoutExpired:
        p.terminate()
        lines = p.communicate()

    for out in lines:
        if b'malloc' in out or b'corrupt' in out or b'free()' in out or b'munmap_chunk()' in out or b'mremap_chunk()' in out:
            # currently not interested in aborts
            #return 'heap:abort'
            return False

    if p.returncode == -11:
        return 'segfault'

    return False

# this will run sudoedit in gdb to analyse the heap objects
def run_sudoedit(arg, env):
    print("-------------")
    # call gdb and load the sudoedit gef extension
    _cmd = ["/usr/bin/gdb"]
    _cmd += ["-ex", 'source /pwd/gef/sudoedit.py']
    _cmd += ["-ex", "set breakpoint pending on"]
    # add the environment vars within gdb
    _cmd += ["-ex", "unset environment"]
    for e in env:
        _cmd += ["-ex", f"set environment {e} = {env[e]}"]
    # execute the heap trace exension
    _cmd += ["-ex", "sudoedit"]
    # run sudoedit
    _cmd += ["-ex", "r "+" ".join([f"'{a}'" for a in arg])]
    #_cmd += ["-ex", "bt"]
    _cmd += ["-ex", "continue"]
    _cmd += ["-ex", "echo BACKTRACE_START_HERE\n"]
    _cmd += ["-ex", "bt"]
    _cmd += ["-ex", "echo BACKTRACE_END_HERE\n"]
    _cmd += ["/usr/local/bin/sudoedit"]

    # execute it
    p = subprocess.Popen(_cmd, bufsize=0, 
            stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    try:
        # send some newlines and check if we get any output
        lines = p.communicate(b"x\nx\nx\nx\n", timeout=4)
    except subprocess.TimeoutExpired:
        # terminate on timeout
        p.terminate()
        lines = p.communicate()
    
    reason = 'weird'
    backtrace = []
    in_backtrace = False
    for line in lines[0].splitlines():
        print(line.decode('utf-8'))
        if b'SIGSEGV, Segmentation fault' in line:
            reason = 'segfault'
        if b'SIGABRT, Aborted' in line:
            reason = 'abort'

        if b'BACKTRACE_END_HERE' in line:
            in_backtrace = False
        if in_backtrace:
            backtrace.append(line.decode('utf-8'))
        if b'BACKTRACE_START_HERE' in line:
            in_backtrace = True

    if os.path.isfile('/tmp/heap'):

        # read the heap data collected by the gef extension
        """
        example /tmp/heap
        sudoersparse sudo_file_parse sudoers_policy_init sudoers_policy_open policy_open out>,
        push_include_int sudoerslex sudoersparse sudo_file_parse sudoers_policy_init sudoers_policy_open policy_open out>,
        sudo_getgrouplist2_v1 fill_group_list <user_details>) <user_details>) main
        """
        with open('/tmp/heap','r') as f:
            heap = f.read()
            lines = heap.splitlines()
        
        # extract the backtrace from the crash location
        _backtrace_short = ' '.join([i.split()[3] for i in backtrace if len(i.split())>3 and i.split()[1].startswith('0x')])
        # shorten the backtrace to use as a filename
        backtrace_short = "".join(x for x in _backtrace_short if x.isalnum() or x==' ' or x=='_')[:100]
        
        # take the filename based on the backtrace
        # fname = f"{FOLDER}/{reason}:{backtrace_short}"
        
        # take the filename from the first heap object after our buffer
        fname = f"{FOLDER}/{reason}:{backtrace_short}"
        dump_file(fname, heap, backtrace, arg, env)

        # dump the args and env in a .json file for automated reproduction
        with open(f'{FOLDER}/{reason}:{backtrace_short}.json', 'a+') as f:
            test = {}
            test['arg'] = arg
            test['env'] = env
            f.write(json.dumps(test))
            f.write('\n')

            
ALPHABET = '0123456789ABCDEFGHIKLMNOPQRSTUVWXYZ'
# fuzz loop
while True:
    # select random size values
    arg1 = random.choice(ARG1)
    rand_arg2_size = random.choice(_SIZES)
    rand_arg3_size = random.choice(_SIZES)
    # random sizes for env vars
    rand_envKey_size, rand_envVal_size = random.choice(_SIZES), random.choice(_SIZES)
    rand_LC_ALL_size = random.choice(_SIZES)
    rand_LOCPATH_size = random.choice(_SIZES)
    rand_TZ_size = random.choice(_SIZES)
    arg = []
    env = {}

    # arguments
    # ... -s AAAAAAA\ ...
    if arg1:
        arg.append(arg1)
    arg.append("-s")
    arg.append(random.choice(ALPHABET)*rand_arg2_size + "\\")
    if rand_arg3_size:
        arg.append(random.choice(ALPHABET)*rand_arg3_size)
        
    # environment variables
    if rand_LC_ALL_size:
        env["LC_ALL"] = random.choice(ALPHABET)*rand_LC_ALL_size
    if rand_LOCPATH_size:
        env["LOCPATH"] = random.choice(ALPHABET)*rand_LOCPATH_size
    if rand_TZ_size:
        env["TZ"] = random.choice(ALPHABET)*rand_TZ_size
    if rand_envKey_size:
        env[random.choice(ALPHABET)*rand_envKey_size] = random.choice(ALPHABET)*rand_envVal_size
        
    # check if sudoedit crashes
    crash = sudoedit_crash_check(arg, env)
    if crash:
        print(f"we got a {crash}, check heap")
        run_sudoedit(arg, env)

