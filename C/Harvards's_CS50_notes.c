#include <stdlib.h>
#include <stdio.h>

int main(void) 
{
    // Getting string input from a user 
    char answer[20] = get_string("What is your name?\n");
    printf("Hello, %s", answer);

    printf("Hello, world!");

}