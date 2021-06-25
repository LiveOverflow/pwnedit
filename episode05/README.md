# Episode 5 - Found a Crash Through Fuzzing? Minimize AFL Testcases!

We found our first real crash in sudo with afl: [`id:000000,sig:06,src:000083+000451,time:23448104,op:splice,rep:8`](id:000000,sig:06,src:000083+000451,time:23448104,op:splice,rep:8). To better analyse this crash it's very useful to minimize the testcase. We are using `afl-tmin` to do that.

- [Video](https://www.youtube.com/watch?v=YeEGDfPqR0E)
- [Blog Article](https://liveoverflow.com/minimizing-afl-testcases-sudo5/)

## Commands

I'm lazy and don't want to type/copy the whole crash filename, so we can use `*` to expand the filename from `id:000000*` to `id:000000,sig:06,src:000083+000451,time:23448104,op:splice,rep:8`.

```bash
hexdump -C id:000000*
# 00000000  73 df 31 31 73 75 64 80  73 75 64 80 5e 5e 3d 5f  |s.11sud.sud.^^=_|
# 00000010  5e 5e 55 5e 5e 5e 73 75  64 6f 01 92 85 64 6f 65  |^^U^^^sudo...doe|
# 00000020  64 69 74 00 2d 41 00 2d  73 00 80 65 00 2d 67 00  |dit.-A.-s..e.-g.|
# 00000030  2d 5c 00 2d 68 00 2d 42  5e 5e 55 5e 5e 8c 6d 64  |-\.-h.-B^^U^^.md|
# 00000040  6f 01 92 75 64 6f 65 64  69 74 00 2d 41 00 2d 62  |o..udoedit.-A.-b|
# 00000050  00 2d 65 00 2d 00 2d 31  73 75 64 80 73 75 64 80  |.-e.-.-1sud.sud.|
# ...
afl-tmin -i id:000000* -o minimized.testcase -- /pwd/sudo-1.8.3p2/src/sudo
hexdump -C minimized.testcase
# 00000000  30 65 64 69 74 00 2d 73  00 30 30 30 30 30 5c 00  |0edit.-s.00000\.|
# 00000010  30 30 30 30 30 30 30 30  30 30 30 30 30 30 30 30  |0000000000000000|
# *
# 00000040  30                                                |0|
```

As can be seen after minimizing it [`minimized.testcase`](minimized.testcase), we have a very clean testcase. `./0edit -s 00000\\ 0000000000000000000000...`. Unfortunately it's not a 0day, because this looks like the known bug.

