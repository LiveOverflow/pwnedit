# pwnedit

CVE-2021-3156 - Sudo Baron Samedit

Before heading into the technical details, you can watch a brief summary here: https://www.youtube.com/watch?v=TLa2VqcGGEQ

## Episodes

Full playlist on [YouTube here](https://www.youtube.com/playlist?list=PLhixgUqwRTjy0gMuT4C3bmjeZjuNQyqdx).

- \[ [Files](episode01) | [Blog](https://liveoverflow.com/why-pick-sudo-research-target-part-1/) | [Video](https://www.youtube.com/watch?v=uj1FTiczJSE) \] Why Pick sudo as Research Target?
- \[ [Files](episode02) | [Blog](https://liveoverflow.com/how-fuzzing-with-afl-works/) | [Video](https://www.youtube.com/watch?v=COHUWuLTbdk) \] How Fuzzing with AFL works
- \[ [Files](episode03) | [Blog](https://liveoverflow.com/troubleshooting-afl-fuzzing-problems/) | [Video](https://www.youtube.com/watch?v=COHUWuLTbdk) \] Troubleshooting AFL Fuzzing Problems
- \[ [Files](episode04) | [Blog](https://liveoverflow.com/finding-buffer-overflow-with-fuzzing/) | [Video](https://www.youtube.com/watch?v=Do1Ri8TCF0Q) \] Finding Buffer Overflow with Fuzzing
- \[ [Files](episode05) | [Blog](https://liveoverflow.com/minimizing-afl-testcases-sudo5/) | [Video](https://www.youtube.com/watch?v=YeEGDfPqR0E) \] Found a Crash Through Fuzzing? Minimize AFL Testcases
- \[ [Files](episode06) | [Blog](https://liveoverflow.com/fuzzer-crash-root-cause-analysis-with-asan-addresssanitizer/) | [Video](https://www.youtube.com/watch?v=_W3D_0erZ00) \] Root Cause Analysis With AddressSanitizer (ASan)
- \[ [Files](episode07) | [Blog](https://liveoverflow.com/understanding-pointer-magic/) | [Video](https://www.youtube.com/watch?v=zdzcTh9kUrc) \] Understanding C Pointer Magic Arithmetic
- \[ [Files](episode07) | Blog | [Video](https://www.youtube.com/watch?v=zdzcTh9kUrc) \] Reaching Vulnerable Code in sudo (C code review)
- ... coming soon

## Requirements

Install [Docker](https://docs.docker.com/get-docker/) and make sure it is running with `docker ps`.

## Usage Instructions

Each episode folder contains files and code snippets used in the video. Most important is the _Dockerfile_, which can be used to run an isolated system vulnerable to the sudoedit vulnerability.

If you want to betetr understand how docker works, checkout these videos:

- [Introduction to Docker for CTFs](https://www.youtube.com/watch?v=cPGZMt4cJ0I)
- [How Docker Works - Intro to Namespaces](https://www.youtube.com/watch?v=-YnMr1lj4Z8)

This project uses a `Makefile` in each episode, to easier work with docker. You can build and run a particular episode's docker container with thes follwing commands.

```bash
cd episode01
sudo make
```

To get a root shell you can then run

```bash
sudo make root
```

Or be a regular user

```bash
sudo make attach
```

Feel free to check the `Makefile` and execute the docker commands directly.
