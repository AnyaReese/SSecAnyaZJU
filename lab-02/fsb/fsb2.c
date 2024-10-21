#include <stdio.h>
#include <unistd.h>
#include <string.h>

#define BUFFER_SIZE 256

void init()
{
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
    alarm(30);
}

int main()
{
    int sz;
    char buffer[BUFFER_SIZE];
    init();

    while (1)
    {
        memset(buffer, '\0', BUFFER_SIZE);
        read(0, buffer, BUFFER_SIZE);
	printf(buffer);
    }


    return 0;
}
