// gcc -o uinit uinit.c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <fcntl.h>

struct user_info
{
    char name[0x20];
    char password[0x20];
    char *intro;
    char motto[0x18];
};

#define MAXUNUM (16)
struct user_info *infos[MAXUNUM];

void prepare()
{
    setvbuf(stdout, 0ll, 2, 0ll);
    setvbuf(stdin, 0ll, 2, 0ll);
    alarm(120);
}

void getline_wrap(int fd, char *buf, int max)
{
    char c;
    int i = 0;
    int err;
    while (i < max)
    {
        err = read(fd, &c, 1);
        if (err < 0)
            break;
        if (c == '\n')
        {
            buf[i] = 0;
            return;
        }
        buf[i++] = c;
    }
    buf[i] = 0;
}

void user_add()
{
    int index = -1;

    for (int i = 0; i < MAXUNUM; i++)
    {
        if (!infos[i])
        {
            index = i;
            break;
        }
    }

    if (index == -1)
    {
        printf("sorry, no room for new user\n");
        return;
    }

    struct user_info *info = malloc(sizeof(struct user_info));
    if (info == NULL)
    {
        goto oom2;
    }
    printf("name > ");
    read(0, info->name, 0x20);
    printf("password > ");
    read(0, info->password, 0x20);
    char *intro = malloc(0x40);
    if (intro == NULL)
    {
        goto oom1;
    }
    printf("introduction > ");
    read(0, intro, 0x40);
    info->intro = intro;
    printf("motto > ");
    read(0, info->motto, 0x18);

    infos[index] = info;
    printf("user %s created at index %d\n", info->name, index);
    return;

oom1:
    free(info);
oom2:
    printf("sorry, no enough memory for new user\n");
    return;
}

void user_del()
{
    int index;
    struct user_info *info;
    char password[0x20] = {0};

    printf("index > ");
    scanf("%d", &index);

    if (!infos[index])
    {
        printf("uset not exists\n");
        return;
    }
    info = infos[index];

    printf("password > ");
    read(0, password, 0x20);

    if (strcmp(password, info->password))
    {
        printf("password incorrect!\n");
        return;
    }

    printf("user %s deleted at index %d\n", info->name, index);
    free(info->intro);
    free(info);
    infos[index] = NULL;
    return;
}

void user_show()
{
    int index;
    struct user_info *info;
    char password[0x20] = {0};

    printf("index > ");
    scanf("%d", &index);

    if (!infos[index])
    {
        printf("uset not exists\n");
        return;
    }
    info = infos[index];

    printf("password > ");
    read(0, password, 0x20);

    if (strcmp(password, info->password))
    {
        printf("password incorrect!\n");
        return;
    }

    printf("user name: ");
    write(1, info->name, 0x20);
    printf("\n");
    printf("user motto: ");
    write(1, info->motto, 0x20);
    printf("\n");
    printf("user intro: ");
    write(1, info->intro, 0x40);
}

void user_edit()
{
    int index;
    struct user_info *info;
    char password[0x20] = {0};

    printf("index > ");
    scanf("%d", &index);

    if (!infos[index])
    {
        printf("uset not exists\n");
        return;
    }
    info = infos[index];

    printf("password > ");
    getline_wrap(0, password, 0x20);

    if (strcmp(password, info->password))
    {
        printf("password incorrect!\n");
        return;
    }

    printf("new name > ");
    getline_wrap(0, info->name, 0x20);
    printf("new introduction > ");
    getline_wrap(0, info->intro, 0x40);
    printf("new motto > ");
    getline_wrap(0, info->motto, 0x18);
    infos[index] = info;
}

void show_choices()
{
    printf("[ 1 ] create user\n");
    printf("[ 2 ] delete user\n");
    printf("[ 3 ] present user\n");
    printf("[ 4 ] edit user\n");
    printf("[ 5 ] leave\n");
    printf("> ");
}

int main(int argc, char *argv[])
{
    char choice;
    prepare();

    /**
     * allocate flag data here
     */
    char* flag = malloc(0x40);
    sprintf(flag, "the sacred and awesome flag is %s\n", getenv("FLAG"));
    // ....
    free(flag);

    while (1)
    {
        show_choices();
        scanf("%d", &choice);
        switch (choice)
        {
        case 1:
            user_add();
            break;
        case 2:
            user_del();
            break;
        case 3:
            user_show();
            break;
        case 4:
            user_edit();
            break;
        case 5:
            return 0;
        default:
            printf("bad input %c\n", choice);
            exit(-1);
        }
    }
}
