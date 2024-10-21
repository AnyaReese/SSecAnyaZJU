#include <stdio.h>
#include <unistd.h>
int var = 0x1234;

int main()
{
    long long x = 0x114514;
    char buf[64];
    read(0, buf, 64);
    printf(buf);
    printf("var = 0x%x\n", var);
    return 0;
}
