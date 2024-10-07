length = int(input())

calculated_threes = [1]

for index in range(0, length):
  k = int(input())
  
  checkInteger = calculated_threes[-1] 
  while(len(calculated_threes) < k):
    checkInteger += 1
    if checkInteger % 10 != 3 and checkInteger % 3 != 0:
      calculated_threes.append(checkInteger)

  print(calculated_threes[k - 1])