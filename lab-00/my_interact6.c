#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <unistd.h>
#include <fcntl.h>
#include <errno.h>

void prepare()
{
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
}

void readline(char *buf, int max, int fd)
{
    int i;
    char cell;

    for (i = 0; i < max; i++)
    {
        read(fd, &cell, 1);
        buf[i] = cell;
        if (cell == '\n')
            break;
    }
}

int main(int argc, char *argv[])
{
    pid_t pid;
    int fds1[2];
    int fds2[2];

    prepare();

    /* fds[0] -> read end
     * fds[1] -> write end
     */
    pipe(fds1);  // see pipe manual
    pipe(fds2);

    pid = fork();

    if (pid == 0)
    {
        /* child process */
        dup2(fds1[1], STDOUT_FILENO); // write end redirect to output
        dup2(fds2[0], STDIN_FILENO);  // read end redirect to input
        close(fds1[0]);
        close(fds1[1]);
        close(fds2[0]);
        close(fds2[1]);
        execlp("./interact5.elf", "./interact5.elf", NULL); // run interact4 program
        exit(-1);
    }
    else
    {
        /* parent process */
        close(fds1[1]);
        close(fds2[0]);

        // when parent process write to fds2[1], it just like to put input to
        // child process, which is interact4
        // when parent process read fds1[0], it just like to get output from
        // child process, which is interact4
        ssize_t write_bytes, read_bytes;
        char buffer[32] = {0};
        read_bytes = read(fds1[0], buffer, 64);
        write(STDOUT_FILENO, buffer, read_bytes);

        // we know interact4 want this string, give to it
        /*------- My Code Start Here ------*/
        // write(fds2[1], "\xaa\xbb\xcc\xdd\xee\xff\n", 7);
        char payload[9] = {0};
        for (int i = 0; i < 8; i++) {
            payload[i] = buffer[i] ^ 0xaa;
        }
        payload[8] = '\n';
        write(fds2[1], &payload, 9);
        /*-------- My Code End Here --------*/
        read_bytes = read(fds1[0], buffer, 64);
        write(STDOUT_FILENO, buffer, read_bytes);

        // for now, shell already launch, just get command and run it
        // like a shell
        while (1)
        {
            write(STDOUT_FILENO, "> ", 2);
            memset(buffer, 0, sizeof(buffer));
            read(STDIN_FILENO, buffer, sizeof(buffer));
            write(fds2[1], buffer, strlen(buffer));
            read_bytes = read(fds1[0], buffer, 64);
            write(STDOUT_FILENO, buffer, read_bytes);
        }
    }
}
