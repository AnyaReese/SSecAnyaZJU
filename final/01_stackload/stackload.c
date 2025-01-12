#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#define LENGTH 256

void welcome() {
    char buffer[20] = {0};
    for (int i = 0; i <= 2; i++)
    {
        printf("Please input data:\n");
        read(0, buffer, LENGTH);
        printf("Buffer content:%s", buffer);
    }
}

int main() {
    setvbuf(stdin, 0LL, 2, 0LL);
    setvbuf(stdout, 0LL, 2, 0LL);
    setvbuf(stderr, 0LL, 2, 0LL);
    printf("Welcome to the stack area!\n");
    welcome();
    return 0;
}