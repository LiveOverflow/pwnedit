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

FOLDER = 'fengshui2'


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
def dump_file(fname, lines, ptrs, arg, env, key):
    # create the folders if they don't exist
    directory = os.path.dirname(fname)
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    # don't write the dump file if it's already too large
    if os.path.isfile(fname) and Path(fname).stat().st_size > 200000:
        return

    # write to file
    with open(fname, 'a+') as f:
        f.write("----------------------------\n")
        f.write(lines[1].decode('ascii'))
        if key:
            distance = ptrs[key] - ptrs[b'user_args']
            f.write(f"user_args < {key.decode('ascii')}\n")
            f.write(f"distance: 0x{distance:x}\n")
        if key:
            f.write(f"0x{ptrs[b'user_args']:016x} < 0x{ptrs[key]:016x}\n")
        f.write("args: sudoedit ")
        f.write(" ".join(arg))
        f.write("\n\n")
        for k in env:
            f.write(f"{k}={env[k]}\n")
        f.write("\n")
        f.write(lines[0].decode('ascii'))
        f.write("\n")

        test = {}
        test['arg'] = arg
        test['env'] = env
        f.write(json.dumps(test))
        f.write("\n\n")

# this will run sudoedit with a set of arguments and environment variables
def run_sudoedit(arg, env):
    print("-------------")
    # disable stdout buffering with stdbuf wrapping around sudoedit
    # and add the commandline arguments
    _cmd = ["/usr/bin/stdbuf", "-o0", "/usr/local/bin/sudoedit"] + arg

    # execute it
    p = subprocess.Popen(_cmd, env=env, bufsize=0, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    try:
        # send some newlines and check if we get any output
        lines = p.communicate(b"x\nx\nx\nx\n", timeout=0.1)
    except subprocess.TimeoutExpired:
        # terminate on timeout
        p.terminate()
        lines = p.communicate()
    
    if p.returncode == -11:
        print(f"SEGFAULT")

    # read the list of function pointers
    ptrs = {}
    skipping = True
    for line in lines[0].splitlines():
        key,val = line.split(b'=')
        if key == b'user_args':
            skipping = False
        if not skipping:
            ptrs[key] = int(val,16)
        
    
    
    # go through all function pointers
    if ptrs and b'user_args' in ptrs:
        for key in ptrs:
            if key != b'user_args':
                # is our overflow buffer before a function pointer?
                if ptrs[b'user_args'] < ptrs[key]:
                    distance = ptrs[key] - ptrs[b'user_args']
                    if distance<14000:
                        fname = f'{FOLDER}/{distance}'
                        dump_file(fname, lines, ptrs, arg, env, key)

                        for line in lines[1].splitlines():
                            if b'abort' in line or b'malloc' in line or b'corrupt' in line or b'free()' in line or b'munmap_chunk()' in line or b'mremap_chunk()' in line:
                                fname = f"{FOLDER}/abort/{line.decode('utf-8')}"
                                dump_file(fname, lines, ptrs, arg, env, None)
                                return
                        
                        # did we get a segfault?
                        if p.returncode == -11:
                            fname = f"{FOLDER}/crashes/segfault_{distance}"
                            dump_file(fname, lines, ptrs, arg, env, None)
                            return
                            
                        return

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
        
    # run sudoedit
    run_sudoedit(arg, env)

