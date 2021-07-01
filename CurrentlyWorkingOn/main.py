studentNames = []
studentMarksTest1 = []
studentMarksTest2 = []
studentMarksTest3 = []
totalScoreForEveryStudent = []

amountOfStudents = 3

tempHighestTotalScore = 0
indexOfHighestScoreHoldersName = None
indexCounter = 0

for x in range(amountOfStudents):
    inputName = input('Enter the name of a child: ')
    studentNames.append(inputName)
    while True:
        inputTest1 = int(input(f"Enter {inputName}'s mark for Test 1: "))
        if inputTest1 > 20:
            print('Error: Mark score too high')
        elif inputTest1 < 0:
            print('Error: Less than zero score')
        else:
            break
    studentMarksTest1.append(inputTest1)
    while True:
        inputTest2 = int(input(f"Enter {inputName}'s mark for Test 2: "))
        if inputTest2 > 25:
            print('Error: Mark score too high')
        elif inputTest2 < 0:
            print('Error: Less than zero score')
        else:
            break
    studentMarksTest2.append(inputTest2)
    while True:
        inputTest3 = int(input(f"Enter {inputName}'s mark for Test 3: "))
        if inputTest3 > 35:
            print('Error: Mark score too high')
        elif inputTest3 < 0:
            print('Error: Less than zero score')
        else:
            break
    studentMarksTest3.append(inputTest3)
for x in range(amountOfStudents):
    tempTotal = studentMarksTest1[x] + studentMarksTest2[x] + studentMarksTest3[x]
    print(f"NAME: {studentNames[x]} - SCORE: {tempTotal}")
    totalScoreForEveryStudent.append(tempTotal)
tempTotal = 0
for x in totalScoreForEveryStudent:
    tempTotal += x 
print(f"The average total score for the whole class is {tempTotal/amountOfStudents}")

for x in totalScoreForEveryStudent:
    indexCounter += 1 
    if x > tempHighestTotalScore:
        tempHighestTotalScore = x
        indexOfHighestScoreHoldersName = indexCounter
    else:
        pass

print(f"The student with the highest total score is {studentNames[indexOfHighestScoreHoldersName]}, with a score of {tempHighestTotalScore}")