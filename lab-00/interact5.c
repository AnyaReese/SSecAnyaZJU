#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#include <unistd.h>

void prepare()
{
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
    srand(time(NULL));
}

int main(int argc, char* argv[])
{
    char password[8];
    char buffer[32];
    char cell;

    prepare();

    for (int i = 0; i < 8; i++)
    {
       password[i] = rand() & 0xff;
       cell = password[i] ^ 0xaa;
       write(STDOUT_FILENO, &cell, 1);
    }

    printf("Enter your password: ");
    scanf("%s", buffer);

    if (!memcmp(buffer, password, 8)) {
        printf("Correct~ launch shell\n");
        system("/bin/sh");
    }
    else {
        printf("Wrong!\n");
	exit(-1);
    }
}
