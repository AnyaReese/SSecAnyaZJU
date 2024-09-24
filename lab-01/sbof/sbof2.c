#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <string.h>

#define LENGTH 256

void prepare()
{
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
    alarm(30);
}

int main(int argc, char **argv)
{
    char buffer[LENGTH];

    prepare();
    printf("gift address: %p\n", buffer);
    gets(buffer);
    return 0;
}