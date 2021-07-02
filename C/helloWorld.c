#include <stdio.h>
#include <stdlib.h>

int main() {

    int unknownNum = 7;
    int usrGuess;
    int attemptNum = 0;

    while (1) {
        if (usrGuess == unknownNum) {
            printf("You have won the game GG");
            break;
        } else if (attemptNum >= 3) {
            printf("You have lost the game lol get good");
            break;
        }
        printf("Please enter you number: ");
        scanf("%d", &usrGuess);
        attemptNum++;
    }

    return 0;
}