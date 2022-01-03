```
cd /pwd/sudo-1.8.31p2
make clean && make && make install
```

```
cd /pwd
python3 fengshui3.py
```

Install gef

```
bash -c "$(curl -fsSL http://gef.blah.cat/sh)"
```

set the plugins directory to our gef location

```
gdb -ex 'gef config gef.extra_plugins_dir "/pwd/gef"' -ex 'gef save' -ex quit
```
