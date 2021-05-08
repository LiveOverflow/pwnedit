# Episode 2 - How Fuzzing with AFL works

Let's continue our `sudo` research. But first we need to fix the [afl](https://github.com/google/AFL) issue from last episode.

- [Video](https://www.youtube.com/watch?v=COHUWuLTbdk)
- [Blog Article](https://liveoverflow.com/how-fuzzing-with-afl-works/)

## Commands

Make sure to also check the file changes and commands from `episode01`!
In order to be able to find the sudoedit functionality through fuzzing, we have to fix some of our fuzzing issues.

First we have to adjust the `rc` start value in [`argv-fuzz-inl.h`](argv-fuzz-inl.h)

```c
int   rc  = 0; /* include argv[0] */
```

And we need to patch the program name functionality in sudo, as can be seen in the diff below. We basically want to remove `getprogname()` and `__progname`, and always use the fallback `argv[0]`.

```diff
--- ./sudo-1.8.31p2/lib/util/progname.c	2020-06-11 20:18:20.000000000 -0700
+++ ./sudo-1.8.31p2/lib/util/progname.c	2021-03-16 05:35:22.320109856 -0700
@@ -36,43 +36,12 @@
 #include "sudo_compat.h"
 #include "sudo_util.h"

-#ifdef HAVE_GETPROGNAME
-
-void
-initprogname(const char *name)
-{
-# ifdef HAVE_SETPROGNAME
-    const char *progname;
-
-    /* Fall back on "name" if getprogname() returns an empty string. */
-    if ((progname = getprogname()) != NULL && *progname != '\0')
-	name = progname;
-
-    /* Check for libtool prefix and strip it if present. */
-    if (name[0] == 'l' && name[1] == 't' && name[2] == '-' && name[3] != '\0')
-	name += 3;
-
-    /* Update internal progname if needed. */
-    if (name != progname)
-	setprogname(name);
-# endif
-    return;
-}
-
-#else /* !HAVE_GETPROGNAME */
-
 static const char *progname = "";

 void
 initprogname(const char *name)
 {
-# ifdef HAVE___PROGNAME
-    extern const char *__progname;

-    if (__progname != NULL && *__progname != '\0')
-	progname = __progname;
-    else
-# endif
     if ((progname = strrchr(name, '/')) != NULL) {
 	progname++;
     } else {
@@ -90,4 +59,3 @@
 {
     return progname;
 }
-#endif /* !HAVE_GETPROGNAME */
```

After fixing the fuzzing harness by including `argv[0]` in the fuzzing testcases:

```bash
# create the input and output folders for afl
mkdir /tmp/in
mkdir /tmp/out
# create an input testcase used for fuzzing
echo -en "sudo\x00-l\x00" > /tmp/in/1.testcase
# we are not including the testcase "sudoedit", to see if AFL can find it
# echo -en "sudoedit\x00-s\x00" > /tmp/in/2.testcase
```

If you have multiple CPUs or CPU cores, we can also use parallel fuzzing

```bash
# start the main fuzzer
afl-fuzz -i /tmp/in -o /tmp/out -M f1 /pwd/sudo-1.8.31p2/src/sudo
# start parallel child fuzzers
afl-fuzz -i /tmp/in -o /tmp/out -S f2 /pwd/sudo-1.8.31p2/src/sudo
afl-fuzz -i /tmp/in -o /tmp/out -S f3 /pwd/sudo-1.8.31p2/src/sudo
afl-fuzz -i /tmp/in -o /tmp/out -S f4 /pwd/sudo-1.8.31p2/src/sudo
```
