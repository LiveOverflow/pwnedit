# gdb -ex 'gef config gef.extra_plugins_dir "/pwd/gef"' -ex 'gef save' -ex quit

__AUTHOR__ = "liveoverflow"
__VERSION__ = 0.1

import collections
import gdb
import json

# persist "database" to the file
def dump(j):
    with open('/tmp/malloc.json', 'w') as f:
        f.write(json.dumps(j))

# load "database" from the file
def load():
    with open('/tmp/malloc.json', 'r') as f:
        j = json.loads(f.read())
    return j

# handler for malloc() breakpoints
class MallocBreakpoint(gdb.Breakpoint):

    def __init__(self, location, *args, **kwargs):
        super(MallocBreakpoint, self).__init__(location, gdb.BP_BREAKPOINT, internal=False)
        self.silent = True
        self.size = None
        self.addr = None
        return

    # malloc() breakpoint triggered
    def stop(self):
        log = {}

        # extract information about this malloc()
        log["size"] = get_register("$rdi")
        log["rip"] = get_register("$rip")
        log["backtrace"] = gdb.execute('bt', to_string=True)
        log['name'] = gdb.newest_frame().older().name()
        
        # set a breakpoint at the malloc() return
        if log['name'] and 'set_cmnd' in log['name']:
            self.retbp = MallocReturnBreakpoint(log=log, overwrite=gdb.newest_frame().older())
            return False
        self.retbp = MallocReturnBreakpoint(log=log)

        return False

# breakpoint for the return of a malloc()
class MallocReturnBreakpoint(gdb.FinishBreakpoint):
    def __init__(self, log, overwrite=False, *args, **kwargs):
        if not overwrite:
            overwrite = gdb.newest_frame()
        super(MallocReturnBreakpoint, self).__init__(overwrite, internal=False)
        self.silent = False
        self.log = log

    def stop(self):
        # extract some information
        self.log['addr'] = get_register("$rax")
        self.log['name'] = gdb.newest_frame().name()
        
        # load the mallocs() we logged before
        MALLOCS = load()
        # add this malloc to the known allocations
        MALLOCS[str(self.log['addr'])] = self.log
        dump(MALLOCS)

        # this is the location of our overflowing buffer
        # now we can dump the heap analysis
        if self.log['name'] and 'set_cmnd' in self.log['name']:
            print("YYYYYYYYYYY WE ARE IN!!!")
            addr = get_register("$rax")
            mallocs = [int(a) for a in MALLOCS]
            mallocs.sort()
            SHOW = 5
            out = ''
            for mall in mallocs:
                if mall > addr and SHOW>0:
                    h = MALLOCS[str(mall)]
                    for line in h['backtrace'].split('\n')[1:]:
                        if line:
                            l = line.split()
                            print(l)
                            if l[3] != '??':
                                out += (l[3]) + " "
                    out += "\n"
                    SHOW -= 1
            out += "\n"
            print(out)
            with open('/tmp/heap' ,'w') as f:
                f.write(out)

            return True
        return False


# set a breakpoint on free()
class FreeBreakpoint(gdb.Breakpoint):
    def __init__(self, location, *args, **kwargs):
        super(FreeBreakpoint, self).__init__(location, gdb.BP_BREAKPOINT, internal=False)
        self.silent = True
        self.size = None
        self.malloc = []
        self.addr = None
        return

    def stop(self):
        log = {}
        log["addr"] = get_register("$rdi")

        # check if the memory freed was allocated before
        MALLOCS = load()
        if str(log["addr"]) in MALLOCS:
            # remove this object from the list of allocated objects
            del MALLOCS[str(log["addr"])]
            dump(MALLOCS)
        return False

# the gdb command that starts the heap trace
class SudoeditCommand(GenericCommand):
    """Tracks a function given in parameter for arguments and return code."""
    _cmdline_ = "sudoedit"
    _syntax_ = f"{_cmdline_}"

    def do_invoke(self, args):
        open('/tmp/test','w').write('a');
        print("SUDOEDIT GEF EXTENSION STARTED")
        dump({})
        self.bkps = []
        # set the breakpoints
        self.bkps.append(MallocBreakpoint(location="__libc_malloc"))
        self.bkps.append(FreeBreakpoint(location="__libc_free"))
        #self.bkps.append(MallocBreakpoint(location="malloc"))
        #self.bkps.append(ReallocBreakpoint(location="__libc_calloc"))
        #self.bkps.append(ReallocBreakpoint(location="__libc_realloc"))
        #self.bkps.append(FreeBreakpoint(location="free"))

        gdb.events.exited.connect(self.cleanup)
        return

    def cleanup(self, events):
        print("CLEANUP!!!")
        for bp in self.bkps:
            bp.delete()
        gdb.events.exited.disconnect(self.cleanup)
        return


if __name__ == "__main__":
    register_external_command(SudoeditCommand())