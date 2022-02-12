import time
import subprocess
import utils
import os
from pathlib import Path

def debug_sudo(pid):
    args = ["/usr/bin/gdb", "-p", f"{pid}"]
    args += ["-ex", 'continue']
    args += ["-ex", "echo BACKTRACE_START_HERE\n"]
    args += ["-ex", "bt"]
    args += ["-ex", "echo BACKTRACE_END_HERE\n"]
    p = subprocess.Popen(args, bufsize=0,
            stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    #time.sleep(0.1)
    utils.set_state(f'continue')
    time.sleep(1)
    try:
        lines = p.communicate(b"x\nx\nx\nx\n",timeout=5)
        print(lines)
    except subprocess.TimeoutExpired:
        p.terminate()
        print('terminated')
        utils.set_state(f'done:')
        return

    
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
    
    _backtrace_short = ' '.join([i.split()[3] for i in backtrace if len(i.split())>3 and i.split()[1].startswith('0x')])
    # shorten the backtrace to use as a filename
    backtrace_short = "".join(x for x in _backtrace_short if x.isalnum() or x==' ' or x=='_')[:100]

    print(backtrace_short)
    if len(backtrace_short)>5:
        fname = f'asd5/segfault:{backtrace_short}'
        if os.path.isfile(fname) and Path(fname).stat().st_size > 200000:
            pass
        else:
            with open(fname,'a') as f:
                for b in backtrace:
                    f.write(b+"\n")
                f.write("\n\n")
    utils.set_state(f'done:{backtrace_short}')

    
while True:
    state = utils.get_state()
    #print(state)
    if state.startswith('pid'):
        print(f"------------------------- {state}")
        pid = state[4:]
        debug_sudo(pid)
    time.sleep(0.1)