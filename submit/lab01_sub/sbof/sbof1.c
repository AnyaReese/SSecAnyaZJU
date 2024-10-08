#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <string.h>

#define LENGTH 64

void target_code(void)
{
    printf("[BINGO]\n");
    execve("/bin/sh", NULL, NULL);
}

void func()
{
    unsigned int len;
    char buffer[LENGTH];
    printf("[*] Please input the length of data:\n");
    scanf("%d", &len);
    printf("    your size: %d\n", len);
    printf("[*] Please input the data:\n");
    read(0, buffer, len);
    printf("    now your size: %d\n", len);
}

void init()
{
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
    alarm(30);
}

int main(int argc, char **argv)
{
    init();
    func();
    return 0;
}