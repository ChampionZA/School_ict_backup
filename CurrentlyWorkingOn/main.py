from typing import MutableMapping
import numba

def squareNum(num):
    return num*num*num

usrInputedNumber = int(input("Enter your number: "))

total = None
temp = str(usrInputedNumber)

for i in len(temp):
    temp = str(usrInputedNumber)
    temp = temp[i]
    total += squareNum[int(temp)]

if (total == usrInputedNumber):
    print("That number is an armstrong number")
else:
    print("That is not an armstrong number")