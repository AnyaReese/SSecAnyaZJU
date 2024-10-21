#include <stdio.h>
#include <unistd.h>
#include <string.h>

#define BUFFER_SIZE 256

char _page[0x1000];
char buffer[BUFFER_SIZE];

void init()
{
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
    alarm(30);
}

void vuln(const char* str) {
    system(str);
}

void do_format() {
    int i = 0;
    while (i < 2)
    {
        memset(buffer, '\0', BUFFER_SIZE);
        read(0, buffer, BUFFER_SIZE);
        printf(buffer);
	i++;
    }
}

int outter() {
    int x = 0;
    do_format();
    return x;
}

int main()
{
    init();
    int x = outter();
    return x;
}
