#include <stdio.h>
#include <unistd.h>
#include <string.h>

void vuln_code(void)
{
    printf("[BINGO]\n");
    execve("/bin/sh", NULL, NULL);
}


void init()
{
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
    // alarm(30);
}

void func() 
{
    char content[128];
    long long x = 0xbeaf;
    printf("address of x is: %p\n", &x);
    memset(content, '\0', 128);
    read(0, content, 128);
    printf(content);

    if (x != 0xbeaf) {
        vuln_code();
    }
}

int main()
{
    init();
    func();
    return 0;
}
