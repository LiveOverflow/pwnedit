# Episode 6 - Fuzzer Crash Root Cause Analysis With ASAN (AddressSanitizer)

Our crash can be triggered by creating a symlink to sudo named `0edit` and calling it with `0edit -s 00000\\ 0000000000000000000000000000000000000000000000000`. But the crash occurs because memory got corrupted, which means the actual overflow happened earlier. In this episode we use ASAN to find the code where it actually overflows and corrupts memory.

- [Video](https://www.youtube.com/watch?v=_W3D_0erZ00)
- Blog Article TBD...

## Commands

To configure and build sudo with ASAN, use the following commands. Note that this command includes `--disabled-shared`. If you do not specify this flag, you will run into the problem shown at the beginning of the video.

```bash
make clean
./configure CFLAGS="-fsanitize=address,undefined" CC=clang --disabled-shared
make
```

If you built the sudo version with the argv wrapper, then call sudo like so:

```
cat minimized.testcase | ./src/sudo
```

If you build regular sudo without any modifications, you can simply run the actual PoC

```
ln -s ./src/sudo ./src/0edit
./src/0edit -s 00000\\ 0000000000000000000000000000000000000000000000000
```

The output should show an AddressSanitizer report
