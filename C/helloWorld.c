#include <stdio.h>
#include <stdlib.h>
#include <cs50.c>

int squareNum(int num);

int main(void)
{
    int total = 0;
    int amountOfNumsWithinUsrInput;
    int usrNumInput;
    while (true)
    {
        usrNumInput = get_int("Please enter your number: ");

        if (usrNumInput > 999)
        {
            printf("Number entered is too big");
        } 
        else if (usrNumInput < 0)
        {
            printf("Number entered too small");
        }
        else if (usrNumInput < 10)
        {
            amountOfNumsWithinUsrInput = 1;
            break;
        }
        else if (usrNumInput < 100)
        {
            amountOfNumsWithinUsrInput = 2;
            break;
        }
        else if (usrNumInput < 1000)
        {
            amountOfNumsWithinUsrInput = 3;
            break;
        }
    }

    string n = (string) usrNumInput;
    for (int i = 0; i < amountOfNumsWithinUsrInput; i++)
    {
        int y = (int) n[i];
        total += squareNum(y);
    }

    if (total == usrNumInput)
    {
        printf("Entered number is an armstrong number");
    } else 
    {
        printf("Entered number is not an armstrong number");
    }
}

int squareNum(int num)
{
    return num*num*num;
}