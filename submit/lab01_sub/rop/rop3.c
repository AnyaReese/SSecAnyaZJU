#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <string.h>

#define LENGTH 64

char _page[0x1000];
char gbuffer[256];

void func()
{
    char buffer[LENGTH];
    printf("> ");
    read(STDIN_FILENO, buffer, LENGTH + 0x10); /* limited */
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
    printf("gift system address: %p\n", system);
    read(STDIN_FILENO, gbuffer, 0x100); /* mid location */
    func();
    return 0;
}
