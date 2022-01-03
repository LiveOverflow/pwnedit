vmmap = """
0x0000555555554000 0x000055555555b000 0x0000000000000000 r-- /pwd/sudo-1.8.31p2/src/sudo
0x000055555555b000 0x00005555555ca000 0x0000000000007000 r-x /pwd/sudo-1.8.31p2/src/sudo
0x00005555555ca000 0x00005555555ea000 0x0000000000076000 r-- /pwd/sudo-1.8.31p2/src/sudo
0x00005555555eb000 0x00005555555ec000 0x0000000000096000 r-- /pwd/sudo-1.8.31p2/src/sudo
0x00005555555ec000 0x00005555555f0000 0x0000000000097000 rw- /pwd/sudo-1.8.31p2/src/sudo
0x00005555555f0000 0x000055555562e000 0x0000000000000000 rw- [heap]
0x00007ffff7c34000 0x00007ffff7c3a000 0x0000000000000000 r-- /usr/lib/x86_64-linux-gnu/libnss_systemd.so.2
0x00007ffff7c3a000 0x00007ffff7c60000 0x0000000000006000 r-x /usr/lib/x86_64-linux-gnu/libnss_systemd.so.2
0x00007ffff7c60000 0x00007ffff7c6c000 0x000000000002c000 r-- /usr/lib/x86_64-linux-gnu/libnss_systemd.so.2
0x00007ffff7c6c000 0x00007ffff7c6f000 0x0000000000037000 r-- /usr/lib/x86_64-linux-gnu/libnss_systemd.so.2
0x00007ffff7c6f000 0x00007ffff7c70000 0x000000000003a000 rw- /usr/lib/x86_64-linux-gnu/libnss_systemd.so.2
0x00007ffff7cb1000 0x00007ffff7cf2000 0x0000000000000000 rw- 
0x00007ffff7cf2000 0x00007ffff7cf5000 0x0000000000000000 r-- /usr/lib/x86_64-linux-gnu/libnss_files-2.31.so
0x00007ffff7cf5000 0x00007ffff7cfc000 0x0000000000003000 r-x /usr/lib/x86_64-linux-gnu/libnss_files-2.31.so
0x00007ffff7cfc000 0x00007ffff7cfe000 0x000000000000a000 r-- /usr/lib/x86_64-linux-gnu/libnss_files-2.31.so
0x00007ffff7cfe000 0x00007ffff7cff000 0x000000000000b000 r-- /usr/lib/x86_64-linux-gnu/libnss_files-2.31.so
0x00007ffff7cff000 0x00007ffff7d00000 0x000000000000c000 rw- /usr/lib/x86_64-linux-gnu/libnss_files-2.31.so
0x00007ffff7d00000 0x00007ffff7d06000 0x0000000000000000 rw- 
0x00007ffff7d14000 0x00007ffff7d46000 0x0000000000000000 r-- /usr/lib/locale/C.UTF-8/LC_CTYPE
0x00007ffff7d46000 0x00007ffff7d48000 0x0000000000000000 rw- 
0x00007ffff7d48000 0x00007ffff7d6d000 0x0000000000000000 r-- /usr/lib/x86_64-linux-gnu/libc-2.31.so
0x00007ffff7d6d000 0x00007ffff7ee5000 0x0000000000025000 r-x /usr/lib/x86_64-linux-gnu/libc-2.31.so
0x00007ffff7ee5000 0x00007ffff7f2f000 0x000000000019d000 r-- /usr/lib/x86_64-linux-gnu/libc-2.31.so
0x00007ffff7f2f000 0x00007ffff7f30000 0x00000000001e7000 --- /usr/lib/x86_64-linux-gnu/libc-2.31.so
0x00007ffff7f30000 0x00007ffff7f33000 0x00000000001e7000 r-- /usr/lib/x86_64-linux-gnu/libc-2.31.so
0x00007ffff7f33000 0x00007ffff7f36000 0x00000000001ea000 rw- /usr/lib/x86_64-linux-gnu/libc-2.31.so
0x00007ffff7f36000 0x00007ffff7f3a000 0x0000000000000000 rw- 
0x00007ffff7f3a000 0x00007ffff7f3c000 0x0000000000000000 r-- /usr/lib/x86_64-linux-gnu/libz.so.1.2.11
0x00007ffff7f3c000 0x00007ffff7f4d000 0x0000000000002000 r-x /usr/lib/x86_64-linux-gnu/libz.so.1.2.11
0x00007ffff7f4d000 0x00007ffff7f53000 0x0000000000013000 r-- /usr/lib/x86_64-linux-gnu/libz.so.1.2.11
0x00007ffff7f53000 0x00007ffff7f54000 0x0000000000019000 --- /usr/lib/x86_64-linux-gnu/libz.so.1.2.11
0x00007ffff7f54000 0x00007ffff7f55000 0x0000000000019000 r-- /usr/lib/x86_64-linux-gnu/libz.so.1.2.11
0x00007ffff7f55000 0x00007ffff7f56000 0x000000000001a000 rw- /usr/lib/x86_64-linux-gnu/libz.so.1.2.11
0x00007ffff7f56000 0x00007ffff7f5d000 0x0000000000000000 r-- /usr/lib/x86_64-linux-gnu/libpthread-2.31.so
0x00007ffff7f5d000 0x00007ffff7f6e000 0x0000000000007000 r-x /usr/lib/x86_64-linux-gnu/libpthread-2.31.so
0x00007ffff7f6e000 0x00007ffff7f73000 0x0000000000018000 r-- /usr/lib/x86_64-linux-gnu/libpthread-2.31.so
0x00007ffff7f73000 0x00007ffff7f74000 0x000000000001c000 r-- /usr/lib/x86_64-linux-gnu/libpthread-2.31.so
0x00007ffff7f74000 0x00007ffff7f75000 0x000000000001d000 rw- /usr/lib/x86_64-linux-gnu/libpthread-2.31.so
0x00007ffff7f75000 0x00007ffff7f79000 0x0000000000000000 rw- 
0x00007ffff7f79000 0x00007ffff7f7b000 0x0000000000000000 r-- /usr/lib/x86_64-linux-gnu/libcrypt.so.1.1.0
0x00007ffff7f7b000 0x00007ffff7f90000 0x0000000000002000 r-x /usr/lib/x86_64-linux-gnu/libcrypt.so.1.1.0
0x00007ffff7f90000 0x00007ffff7faa000 0x0000000000017000 r-- /usr/lib/x86_64-linux-gnu/libcrypt.so.1.1.0
0x00007ffff7faa000 0x00007ffff7fab000 0x0000000000030000 r-- /usr/lib/x86_64-linux-gnu/libcrypt.so.1.1.0
0x00007ffff7fab000 0x00007ffff7fac000 0x0000000000031000 rw- /usr/lib/x86_64-linux-gnu/libcrypt.so.1.1.0
0x00007ffff7fac000 0x00007ffff7fb4000 0x0000000000000000 rw- 
0x00007ffff7fb4000 0x00007ffff7fb5000 0x0000000000000000 r-- /usr/lib/x86_64-linux-gnu/libutil-2.31.so
0x00007ffff7fb5000 0x00007ffff7fb6000 0x0000000000001000 r-x /usr/lib/x86_64-linux-gnu/libutil-2.31.so
0x00007ffff7fb6000 0x00007ffff7fb7000 0x0000000000002000 r-- /usr/lib/x86_64-linux-gnu/libutil-2.31.so
0x00007ffff7fb7000 0x00007ffff7fb8000 0x0000000000002000 r-- /usr/lib/x86_64-linux-gnu/libutil-2.31.so
0x00007ffff7fb8000 0x00007ffff7fb9000 0x0000000000003000 rw- /usr/lib/x86_64-linux-gnu/libutil-2.31.so
0x00007ffff7fb9000 0x00007ffff7fbb000 0x0000000000000000 rw- 
0x00007ffff7fc2000 0x00007ffff7fc9000 0x0000000000000000 r-- /usr/lib/x86_64-linux-gnu/gconv/gconv-modules.cache
0x00007ffff7fc9000 0x00007ffff7fcd000 0x0000000000000000 r-- [vvar]
0x00007ffff7fcd000 0x00007ffff7fcf000 0x0000000000000000 r-x [vdso]
0x00007ffff7fcf000 0x00007ffff7fd0000 0x0000000000000000 r-- /usr/lib/x86_64-linux-gnu/ld-2.31.so
0x00007ffff7fd0000 0x00007ffff7ff3000 0x0000000000001000 r-x /usr/lib/x86_64-linux-gnu/ld-2.31.so
0x00007ffff7ff3000 0x00007ffff7ffb000 0x0000000000024000 r-- /usr/lib/x86_64-linux-gnu/ld-2.31.so
0x00007ffff7ffc000 0x00007ffff7ffd000 0x000000000002c000 r-- /usr/lib/x86_64-linux-gnu/ld-2.31.so
0x00007ffff7ffd000 0x00007ffff7ffe000 0x000000000002d000 rw- /usr/lib/x86_64-linux-gnu/ld-2.31.so
0x00007ffff7ffe000 0x00007ffff7fff000 0x0000000000000000 rw- 
0x00007ffffffde000 0x00007ffffffff000 0x0000000000000000 rw- [stack]
0xffffffffff600000 0xffffffffff601000 0x0000000000000000 --x [vsyscall]
"""

import struct


memmap = []
for mem in vmmap.splitlines():
    if 'r-x' in mem:
        start, end, size, perm, f = mem.split(' ')
        start = int(start, 16)
        end = int(end, 16)
        memmap.append((start, end))

with open('./heap','rb') as f:
    heap = f.read()

n = 0x41

for i in range(0, len(heap), 8):
    heap_addr = i+0x00005555555f0000
    b = heap[i:i+8]
    q = struct.unpack('Q', b)[0]
    for mem in memmap:
        if q>=mem[0] and q<=mem[1]:
            #print(f"0x{heap_addr:016x}: {q:016x} {b}")
            print(f"set *0x{heap_addr:016x} = 0x"+(hex(n)[2:]*5))
            n += 1
    if 0x00005555556131e0 == heap_addr:
            print(f"0x{heap_addr:016x}: our [buffer]")
