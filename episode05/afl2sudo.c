#include "argv-fuzz-inl.h"

int main(int argc, char *argv[], char *envp[])
{
	AFL_INIT_ARGV(); // argv is now the fake argv
    execve("/usr/local/bin/sudo", argv, envp);
}