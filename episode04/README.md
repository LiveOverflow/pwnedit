# Episode 3 - Troubleshooting AFL Fuzzing Problems

We found a crash with [afl](https://github.com/google/AFL), but it turns out to be a bug in the `argv-fuzz-inl.h` file.

- [Video](https://www.youtube.com/watch?v=Do1Ri8TCF0Q)
- [Blog Article](https://liveoverflow.com/finding-buffer-overflow-with-fuzzing/)

## Commands

Make sure to also check the file changes and commands from `episode01` and `episode02`!
The most important change in this episode is to hardcode the user id. This will allow us to run sudo already being root, like it would have been when running as setuid.

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
@@ -522,9 +524,9 @@
     }
     ud->sid = getsid(0);

-    ud->uid = getuid();
+    ud->uid = 1000; //getuid();
     ud->euid = geteuid();
-    ud->gid = getgid();
+    ud->gid = 1000; //getgid();
     ud->egid = getegid();
```

Please checkout `episode02` for details how to start fuzzing.
