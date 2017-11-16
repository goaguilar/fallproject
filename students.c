#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct
{
    char *name;
    char *dorm;
}
student;

int cmp(const void *a, const void *b);

int main(void)
{
    student heads[] =
    {
        {"Stelios", "Branford"},
        {"Maria", "Cabot"},
        {"Anushree", "Ezra Stiles"},
        {"Brian", "Winthrop"}
    };
    printf("Before:\n");
    for (int i = 0; i < 4; i++)
    {
        printf("%s from %s\n", heads[i].name, heads[i].dorm);
    }
    qsort(heads, 4, sizeof(student), cmp);
    printf("After:\n");
    for (int i = 0; i < 4; i++)
    {
        printf("%s from %s\n", heads[i].name, heads[i].dorm);
    }
}

int cmp(const void *a, const void *b)
{
    char arg1 = *(const char*)a;
    char arg2 = *(const char*)b;

    if (strcmp(arg1, arg2) > 0)
    {
        return 1;
    }
    if (strcmp(arg1, arg2) < 0)
    {
        return -1;
    }
    return 0;
}
