#include <sys/mman.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>
#include <stdlib.h>
#define PAGESIZE 4096
int main()
{
    int fd = open("./input.txt", O_RDONLY);
    struct stat sb;
    if (fstat(fd, &sb) == -1)
    {
        perror("couldn't get filesize\n");
    }
    printf("Size of file: %zu - %zu", sb.st_size, sb.st_size / PAGESIZE);
    char *i = mmap(NULL, sb.st_size, PROT_READ, MAP_PRIVATE, fd, 0);
    ftruncate(fd, sb.st_size);
    close(fd);
    char *cur = i;
    size_t numcount = 1;
    while (*cur) //while not EOF
    {
        if (*cur == '\n')
        { //count numbers
            numcount++;
        }
        // printf("%c",*cur);
        cur++;
    }
    int *nums = (int *)malloc(sizeof(int) * numcount);
    int res = 0;
    char res_char[20];
    size_t c = 0;
    size_t rc = 0;
    cur = i;
    while (*cur)
    {
        if (*cur == '\n')
        { //next word
            res_char[c] = '\0';
            nums[rc++] = atoi(res_char);
            c = 0;
            cur += 1;
            continue;
        }
        res_char[c] = *cur;
        cur += 1;
        c++;
    } //add last
    res_char[c] = '\0';
    nums[rc] = atoi(res_char);
    printf("entries: %zu\n", numcount);
    //check how many times next is bigger:
    size_t orig = 0; //info flag if 0 sliding window is used otherwise original is used
    size_t next_bigger = 0;
    size_t last = orig ? nums[0] : nums[0] + nums[1] + nums[2];
    size_t cursum = 0;
    //info original
    if (orig)
        for (size_t i = 1; i < numcount; i++)
        {
            if (nums[i] > last)
            {
                next_bigger++;
            }
            last = nums[i];
        }
    //info 3-sliding window
    printf("%zu", next_bigger);
    for (size_t i = 1; i < numcount - 2; i += 1)
    {
        cursum = nums[i] + nums[i + 1] + nums[i + 2];
        // printf("%zu\n", cursum);
        if (cursum > last)
            ++next_bigger;
        last = cursum;
    }
    printf("next bigger: %zu", next_bigger);
}