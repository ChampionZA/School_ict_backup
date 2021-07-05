#include <string.h>
#include <cs50.c>
#include <stdio.h>

bool String_Difference_Checker(char * a, char * b);

int main(void)
{
    char * s = get_string("", "s: ");
    char * j = get_string("", "j: ");

    if (String_Difference_Checker(s, j))
    {
        printf("No Difference Detected");
    }
    else
    {
        printf("Difference Detected");
    }
}

bool String_Difference_Checker(char * a, char * b)
{
    if (strlen(a) != strlen(b))
    {
        return false;
    }

    for (int i = 0, n = strlen(b); i < n; i++)
    {
        if (a[i] != b[i])
        {
            return false;
        }
    }

    return true;
}