#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <string.h>

#define LENGTH 64

static char gstr[] = "/bin/sh";
void target_code(unsigned long arg)
{
    system("/bin/ls");
}

void func()
{
    unsigned int len;
    char buffer[LENGTH];
    printf("[*] Please input the length of data:\n");
    scanf("%d", &len);
    printf("[*] Please input the data:\n");
    read(0, buffer, len);
}

void prepare()
{
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
    alarm(30);
}

int main(int argc, char **argv)
{
    prepare();
    func();
    return 0;
}