#include <stdio.h>
#include <stdlib.h>

int big(int num1, int num2, int num3) {
    if (num1 >= num2 && num1 >= num3) {
        return num1;
    } else if (num2 >= num1 && num2 >= num3) {
        return num2;
    } else {
        return num3;
    }
}

int main() {
    
    int usrNumEntry1;
    int usrNumEntry2;
    int usrNumEntry3;

    printf("Please enter two numbers separated by a space: ");
    scanf("%d%d%d", &usrNumEntry1, &usrNumEntry2, &usrNumEntry3);

    printf("Answer: %d", big(usrNumEntry1, usrNumEntry2, usrNumEntry3));

    return 0;
}