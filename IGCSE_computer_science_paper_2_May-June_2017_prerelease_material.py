childrenWantingToComeOnTrip = {}
costOfCoach = 550
costOfEntryTicket = 30

while True:
    usrChoice = input('Task 1 [1], Task 2 [2]: ')
    if usrChoice == '1':
        while True:
            estimatedNumberOfStudentsTakingPart = int(input('How many students are going to be taking part: '))
            if estimatedNumberOfStudentsTakingPart > 40:
                print('Error: There are too many children taking part')
            elif estimatedNumberOfStudentsTakingPart <= 0:
                print('Error: Why are you doing a trip when there are no kids?')
            else:
                break
        numOfFreeTickets = estimatedNumberOfStudentsTakingPart // 10
        totalCost = ((estimatedNumberOfStudentsTakingPart - numOfFreeTickets) * costOfEntryTicket) + costOfCoach
        recomendedPricePerStudent = totalCost / estimatedNumberOfStudentsTakingPart
        print(f'The minimum that each student has to pay to not make a loss will be ${recomendedPricePerStudent}')

    if usrChoice == '2':
        while True:
            numStudentsWantToCome = int(input('How many students want to come?: ')
            if numStudentsWantToCome > 40:
                print('Error: amount of students over the limit')
            elif numStudentsWantToCome <= 0:
                print('Error: You cant have no kids on the trip')
            else:
                break
        for _ in range(numStudentsWantToCome):
            studentName = input('What is the name of a student that has asked to join?: ')
            while True:
                studentPaid = input(f'Has {studentName} payed to go on the trip [y] or [n]: ')
                if studentPaid == 'y' or studentPaid == 'Y':
                    childrenWantingToComeOnTrip[studentName] = True
                    break
                elif studentPaid == 'n' or studentPaid == 'N':
                    childrenWantingToComeOnTrip[studentName] = False
                    break
                else:
                    print('Please enter one of the options')