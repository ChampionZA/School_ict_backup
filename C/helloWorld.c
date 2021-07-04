#include <stdio.h>
#include <stdlib.h>
#include <cs50.c>

int squareNum(int num);

int main(void)
{

    int lenNum;
    int usrEnteredNum;
    int temp;

    while (true)
    {
        usrEnteredNum = get_int("Enter your number: ");
        if (usrEnteredNum < 0 || usrEnteredNum > 999)
        {
            printf("Invalid input");
        }
        else
        {
            break;
        }
    }

    lenNum = floor (log10 (abs (usrEnteredNum))) + 1;

    for (int i = 0; i < lenNum; i++)
    {
    }

}

int timesNum(int num, int powerOf)
{
    int total = 0;
    for (int i = 0; i < powerOf; i++)
    {
        total *= num;
    }
    return total;
}