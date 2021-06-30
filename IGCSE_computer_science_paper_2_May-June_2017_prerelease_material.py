costOfCoach = 550
costOfEntryTicket = 30

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