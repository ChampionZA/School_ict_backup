yields = {}
testing_dict = {1:[2.3, 2.4, 5.6, 6.5], 2:[6.2, 4.5, 5.2, 7.9]}

hightestVolume = 0 
lowestVolume = float('inf')

def adding_yield_entry():
  while True:
    userCowIdEntry = int(input('Enter the 3 digit ID of the cow you want to enter [NUMERS ONLY]: '))
    if len(str(userCowIdEntry)) == 3:
      break
    else:
      pass
  userYieldEntry = float(input('Enter the yield for that cow [to ONE decimal place]: '))
  if userCowIdEntry in yields:
    pass
  else:
    yields[userCowIdEntry] = []
  if len(yields[userCowIdEntry]) >= 14:
    print('This cow already has 7 entrys for the week')
  else:
    yields[userCowIdEntry].append(userYieldEntry)

def ending_the_week():
  global tempTotal
  global allCowsTotal
  global amountOfYields
  global hightestVolume
  global lowestVolume
  global hightestVolumeCow
  global lowestVolumeCow
  global cowUnder12Counter
  print()
  print('TOTAL FOR EVERY COW THIS WEEK:')
  allCowsTotal = 0
  amountOfYields = 0
  for i in yields:
    tempTotal = 0
    for x in yields[i]:
      allCowsTotal += x
      tempTotal += x
      amountOfYields += 1
    tempTotal = round(tempTotal, 0)
    tempTotal = str(tempTotal).split('.')[0]
    print(f'Cow: {i} has produced {tempTotal} liters this week')
    if len(yields[i]) != 14:
      for j in range(14 - len(yields[i])):
        yields[i].append('')
  print()
  print('TOTAL FOR ALL COWS THIS WEEK:')
  print(f"{str(round(allCowsTotal, 0)).split('.')[0]} litres")
  print()
  print('AVERAGE OF ALL COWS:')
  print(f"{str(allCowsTotal//amountOfYields).split('.')[0]} litres")
  print()
  print('AVERAGE OF EVERY COW:')
  for i in yields:
    amountOfYields = 0 
    tempTotal = 0 
    for x in yields[i]:
      if x == '':
        pass
      else:
        amountOfYields += 1 
        tempTotal += x
    print(f"Cow: {i} produced an average of {str(round(tempTotal/amountOfYields, 0)).split('.')[0]} litres")
    yields[i].append(round(tempTotal, 1))
    yields[i].append(str(tempTotal//amountOfYields).split('.')[0])
    print()
    if tempTotal < lowestVolume:
      lowestVolume = tempTotal
      lowestVolumeCow = i
    if tempTotal > hightestVolume:
      hightestVolume = tempTotal
      hightestVolumeCow = i

  print(f'Your most productive cow is cow: {hightestVolumeCow} at {hightestVolume} liters yielded')
  print(f"Your least productive cow is cow: {lowestVolumeCow} at {lowestVolume} liters yielded")
  print()
  print('COWS THAT YIELDED LESS THAN 12 LITRES OF MILK FOR FOUR DAYS OR MORE IN THE WEEK:')
  for i in yields:
    cowUnder12Counter = 0
    for x in range(0,13):
      if yields[i][x] == '':
        pass
      elif yields[i][x] < 12:
        cowUnder12Counter += 1 
    if cowUnder12Counter >= 4:
      print(f'Cow: {i} underpreformed')

while True:
  userDecision = input('Do you want to make a yield entry [1], end the week [2]: ')
  if userDecision == '1':
    adding_yield_entry()
  elif userDecision == '2':
    ending_the_week()

  print(yields)