# Episode 4 - Finding Buffer Overflow with Fuzzing

We found a crash with [afl](https://github.com/google/AFL), but it turns out to be a bug in the `argv-fuzz-inl.h` file.

- [Video](https://www.youtube.com/watch?v=Do1Ri8TCF0Q)
- [Blog Article](https://liveoverflow.com/finding-buffer-overflow-with-fuzzing/)

## Commands

This project builds iteratively on the previous episodes. In this episode we found a buffer overflow issue in `argv-fuzz-inl.h`, which we can fix by checking the `rc` counter cannot count too high.

```
while (*ptr) {

    // fix buffer overflow
    if(rc >= MAX_CMDLINE_PAR) {
      break;
    }
    
    ret[rc] = ptr;
```

