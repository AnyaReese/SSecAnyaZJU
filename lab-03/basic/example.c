#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>

#include <fcntl.h>

/* example specific part */
static void *local_alloc_hook(size_t, const void *);
static void local_free_hook(void *, const void *);

#include <malloc.h>
// see https://www.gnu.org/software/libc/manual/html_node/Hooks-for-Malloc.html
void *old_malloc_hook, *old_free_hook;

static void load_hooks()
{
    old_malloc_hook = __malloc_hook;
    old_free_hook = __free_hook;
    __malloc_hook = local_alloc_hook;
    __free_hook = local_free_hook;
}

static void *local_alloc_hook(size_t size, const void *caller)
{
    __malloc_hook = old_malloc_hook;
    __free_hook = old_free_hook;
    void *result = malloc(size);
    printf("[+] caller at %p allocating %x, returns %p\n", caller, size, result);
    __malloc_hook = local_alloc_hook;
    __free_hook = local_free_hook;
    return result;
}

static void local_free_hook(void *ptr, const void *caller)
{
    __malloc_hook = old_malloc_hook;
    __free_hook = old_free_hook;
    free(ptr);
    printf("[+] caller at %p releasing %p\n", caller, ptr);
    __malloc_hook = local_alloc_hook;
    __free_hook = local_free_hook;
}

/* end example specific part */

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
    load_hooks();
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
    memset(info, 0, sizeof(struct user_info));
    printf("name > ");
    getline_wrap(0, info->name, 0x20);
    printf("password > ");
    getline_wrap(0, info->password, 0x20);
    char *intro = malloc(0x40);
    if (intro == NULL)
    {
        goto oom1;
    }
    memset(intro, 0, 0x40);
    printf("introduction > ");
    getline_wrap(0, intro, 0x40);
    info->intro = intro;
    printf("motto > ");
    getline_wrap(0, info->motto, 0x18);

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
    char password[0x20];

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
    char password[0x20];

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

    printf("user name: %s\n", info->name);
    printf("user motto: %s\n", info->motto);
    printf("user intro: %s\n", info->intro);
}

void user_edit()
{
    int index;
    struct user_info *info;
    char password[0x20];

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

int dump_cnt = 0;

void heap_debug()
{
    int maps_fd = open("/proc/self/maps", O_RDONLY);
    if (maps_fd < 0)
    {
        perror("failed to open /proc/self/maps");
        return;
    }

    char line[0x100];
    uint64_t heap_start = 0;

    while (1)
    {
        getline_wrap(maps_fd, line, 0x100);
        if (strstr(line, "[heap]"))
        {
            sscanf(line, "%lx-", &heap_start);
            break;
        }
    }
    close(maps_fd);

    if (heap_start == 0)
    {
        printf("failed to find heap mapping\n");
        return;
    }

    char dumpname[0x40];
    sprintf(dumpname, "dump_%lx_%x.bin", heap_start, dump_cnt++);

    int dump_fd = open(dumpname, O_WRONLY | O_CREAT);
    if (dump_fd < 0)
    {
        perror("failed to open dump file");
        return;
    }

    write(dump_fd, (void *)heap_start, 0x1000);
    close(dump_fd);
    return;
}

int main(int argc, char *argv[])
{
    char choice;
    prepare();
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
        case 6:
            // debug dump
            heap_debug();
            break;
        default:
            printf("bad input %c\n", choice);
            exit(-1);
        }
    }
}
