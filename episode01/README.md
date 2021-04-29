# Episode 1 - Why Pick sudo as Research Target?

Let's talk about how we could end up researching `sudo` and then let's try to use [afl](https://github.com/google/AFL) for fuzzing.

* [Video](https://www.youtube.com/watch?v=uj1FTiczJSE)
* [Blog Article](https://liveoverflow.com/why-pick-sudo-research-target-part-1/)

## Commands

To setup the container for this episode, unpack the sudo source code in the current `episode01` directory.
Then you can run the container with `make run` and get a shell insode the container with `make root`.
The extracted sudo source code is now available in `/pwd/sudo-1.8.31p2`.

```bash
# unpack the sudo sourcecode in the current episode01 folder
tar -xvf sudo-1.8.31p2.tar.gz
# then start the container to work on it
sudo make run
sudo make root
```

Inside the container you can test the crash with:

```bash
sudoedit -s '12345678901234567890\'
# malloc(): invalid size (unsorted)
# Aborted
```

Copy the [`argv-fuzz-inl.h`](argv-fuzz-inl.h) into the sudo source code in `/pwd/sudo-1.8.31p2/src` and then modify [`sudo.c`](sudo.c) as shown below:

```diff
--- ./sudo-1.8.31p2/src/sudo.c	2020-06-12 06:14:53.000000000 -0700
+++ ./sudo-1.8.31p2/src/sudo.c	2021-03-16 06:32:56.655334720 -0700
@@ -68,6 +68,7 @@
 #include "sudo.h"
 #include "sudo_plugin.h"
 #include "sudo_plugin_int.h"
+#include "argv-fuzz-inl.h"
 
 /*
  * Local variables
@@ -134,6 +135,7 @@
 int
 main(int argc, char *argv[], char *envp[])
 {
+	AFL_INIT_ARGV();
     int nargc, ok, status = 0;
     char **nargv, **env_add;
     char **user_info, **command_info, **argv_out, **user_env_out;
```

Now you can try to instrument sudo with [afl](https://github.com/google/AFL) (but this will not work, as shown in the video).

```bash
cd /pwd/sudo-1.8.31p2
CC=afl-gcc ./configure --disable-shared
make
mkdir /tmp/in
mkdir /tmp/out
echo -en "-l\x00" > /tmp/in/1.testcase
afl-fuzz -i /tmp/in -i /tmp/out ./src/sudo
```