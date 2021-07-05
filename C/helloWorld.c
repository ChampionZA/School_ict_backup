#include <string.h>
#include <cs50.c>
#include <stdio.h>

int main(void)
{
    string s = get_string("", "s: ");
    string j = get_string("", "j: ");

    if (s == j)
    {
        printf("No Difference Detected");
    }
    else
    {
        printf("Difference Detected");
    }
}