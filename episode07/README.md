# Episode 7 - Understanding C Pointer Magic Arithmetic

We basically just look at source code and debug with gdb in this episode. No files needed.

- [Video](https://www.youtube.com/watch?v=zdzcTh9kUrc)
- Blog Article

## Commands

Using the [`gef`](https://gef.readthedocs.io/en/master/) `gdb` extension

```bash
# via the install script
$ wget -q -O- https://github.com/hugsy/gef/raw/master/scripts/gef.sh | sh
```

Configure the debug build and disable optimization for easier assembly.

```bash
CFLAGS="-g -O0" ./configure
```
