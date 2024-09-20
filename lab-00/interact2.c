#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void prepare()
{
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
}

int main(int argc, char* argv[])
{
    char password[] = "ssec-welcome";
    char buffer[32];

    prepare();
    printf("Enter your password: ");
    scanf("%s", buffer);

    if (!strncmp(buffer, password, strlen(password))) {
        printf("Correct~ launch shell\n");
        system("/bin/sh");
    }
    else {
        printf("Wrong!\n");
	exit(-1);
    }
}
