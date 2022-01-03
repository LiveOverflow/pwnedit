# pwnedit

CVE-2021-3156 - Sudo Baron Samedit

Before heading into the technical details, you can watch a brief summary here: https://www.youtube.com/watch?v=TLa2VqcGGEQ

## Episodes

1. \[ [Files](episode01) | [Blog](https://liveoverflow.com/why-pick-sudo-research-target-part-1/) | [Video](https://www.youtube.com/watch?v=uj1FTiczJSE) \] Why Pick sudo as Research Target?
2. \[ [Files](episode02) | [Blog](https://liveoverflow.com/how-fuzzing-with-afl-works/) | [Video](https://www.youtube.com/watch?v=COHUWuLTbdk) \] How Fuzzing with AFL works
3. \[ [Files](episode03) | [Blog](https://liveoverflow.com/troubleshooting-afl-fuzzing-problems/) | [Video](https://www.youtube.com/watch?v=COHUWuLTbdk) \] Troubleshooting AFL Fuzzing Problems
4. \[ [Files](episode04) | [Blog](https://liveoverflow.com/finding-buffer-overflow-with-fuzzing/) | [Video](https://www.youtube.com/watch?v=Do1Ri8TCF0Q) \] Finding Buffer Overflow with Fuzzing
5. \[ [Files](episode05) | [Blog](https://liveoverflow.com/minimizing-afl-testcases-sudo5/) | [Video](https://www.youtube.com/watch?v=YeEGDfPqR0E) \] Found a Crash Through Fuzzing? Minimize AFL Testcases
6. \[ [Files](episode06) | Blog | [Video](https://www.youtube.com/watch?v=_W3D_0erZ00) \] Root Cause Analysis With AddressSanitizer (ASan)
7. \[ [Files](episode07) | Blog | [Video](https://www.youtube.com/watch?v=zdzcTh9kUrc) \] Understanding C Pointer Magic Arithmetic
8. \[ [Files](episode08) | Blog | [Video](https://www.youtube.com/watch?v=RZiGBjrOLY8) \] C Code Review - Reaching Vulnerable Code in sudo
9. \[ [Files](episode09) | Blog | [Video](https://www.youtube.com/watch?v=c2Qi7traPls) \] Discussing Heap Exploit Strategies for sudo
10. \[ [Files](episode10) | Blog | [Video](https://www.youtube.com/watch?v=UFyTksTXFTA) \] Developing a Tool to Find Function Pointers on The Heap
11. \[ [Files](episode11) | Blog | [Video](https://www.youtube.com/watch?v=CYWoJ6EYo84) \] Fuzzing Heap Layout to Overflow Function Pointers
12. \[ [Files](episode12) | Blog | [Video](https://www.youtube.com/watch?v=tzUrYsQRHfs) \] Developing GDB Extension for Heap Exploitation
13. \[ [Files](episode13) | Blog | [Video](https://www.youtube.com/watch?v=Y8qljlUjEEM) \] Can We Find a New Exploit Strategy?
14. \[ Files | Blog | [Video](https://www.youtube.com/watch?v=0ti-YgB2iR4) \] Learning about nss (Linux Name Service Switch) During Sudo Exploitation

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
