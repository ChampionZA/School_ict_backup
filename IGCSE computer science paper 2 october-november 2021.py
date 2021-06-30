import re

homeToStartStation = {'c1':1.50, 'c2':3.00, 'c3':4.50, 'c4':6.00, 'c5':8.00}
startStationToEndStation = {'m1':5.75,'m2':12.50,'m3':22.25,'m4':34.50, 'm5':45.00}
endStationToDestination = {'f1':1.50,'f2':3.00,'f3':4.50,'f4':6.00,'f5':8.00}
bookingDetails = {}
accounts = {}

stageCodes = []

generatingNumbers = 0

stageOneSet = False
stageTwoSet = False
stageThreeSet = False
exitVarEnterAccNum = False

def discount(percent, total):
  return '{0:.2f}'.format(total * (percent/100))

def account_creation():
  global personalAccNum
  name = input("Please enter your name [LETTERS ONLY]: ")
  if name == "exit":
    return
  personalAccNum = int(input('Please create your personal account number [NUMBERS ONLY]: '))
  if personalAccNum in accounts:
    print('That account number already exists!!')
    account_creation()
    return
  else:
    pass
  accounts[personalAccNum] = name
  print(f"Thank you, your accounts number is {personalAccNum}")

def making_a_booking():
  global passengerAccountNumber
  global startTime
  global stageCodes
  global stageOne
  global stageTwo
  global stageThree
  global totalCost
  global generatingNumbers
  global areUSure
  global exitVarEnterAccNum

  while True:
    passengerAccountNumber = int(input("Please enter your account NUMBER: "))
    if passengerAccountNumber in accounts:
      break
    else:
      print('That account does not exist (Type "exit" to return)')

  if exitVarEnterAccNum:
    return

  print(f'Welcome {accounts[passengerAccountNumber]}')

  while True:
    startTime = input('Please enter the start time of your journey: ')
    if re.match(r'\d\d:\d\d', startTime):
      break
    else:
      continue

  while True:
    stageOne = input('Please enter the first stage of your journey: ')
    if stageOne in homeToStartStation:
      totalCost += homeToStartStation[stageOne]
      break
    else:
      print("That is not a valid code for stage one!")
  
  while True:
    stageTwo = input('Please enter the second stage of your journey: ')
    if stageTwo == "" or stageTwo in startStationToEndStation:
      break
    else:
      print('You can only enter a valid code or nothing to only use stage one')

  
  if stageTwo == '':
    stageThree = ''
    pass
  else:
    totalCost += startStationToEndStation[stageTwo]

    while True:
      stageThree = input('Please enter the third stage of your journey: ')
      if stageThree == '' or stageThree in endStationToDestination:
        break
      else:
        print('You can only enter a valid code or leave blank if you only need stage one and two')

    if stageThree == '':
      pass
    else:
      totalCost += endStationToDestination[stageThree]    


  print(f"Your unique booking number is {generatingNumbers+1}")

  if int(startTime.split(':')[0]) > 10 or int(startTime.split(':')[0]) == 00:
    totalCost = discount(40, totalCost)
    print('A 40% discount has been applied to the total price')

  bookingDetails[generatingNumbers+1] = [startTime, stageOne, stageTwo, stageThree, passengerAccountNumber, totalCost]

  if bookingDetails[generatingNumbers+1][2] == '' and bookingDetails[generatingNumbers+1][3] == '':
    print(f"It's going to cost you ${totalCost} to go from home to start station")
  elif bookingDetails[generatingNumbers+1][3] == '':
    print(f"It's going to cost you ${totalCost} to go from home to end station")
  else:
    print(f"It's going to cost you ${totalCost} to go from home to destination")

  while True:
    areUSure = int(input('Are you sure the details are correct? [1] yes or [2] no: '))
    if areUSure == 1:
      print('Details have been saved, have a nice day')
      generatingNumbers += 1
      break
    elif areUSure == 2:
      print('No problem, just restart the booking process')
      del bookingDetails[generatingNumbers+1]
      print('Previously entered information has been deleted')
      break
    else:
      print('please enter a valid option')
    

while True:
  # dev note: you can type 69 to get the stored booking details and accounts
  totalCost = 0
  exitVarEnterAccNum = False
  choice = int(input("Would you like to Create a new account [1] or make a booking [2]: "))
  if choice == 1:
    account_creation()
  elif choice == 2:
    making_a_booking()
  elif choice == 69:
    print(f"Booking Details - {bookingDetails}")
    print(f"Accounts - {accounts}")