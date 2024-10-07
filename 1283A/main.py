length = int(input())

for index in range(0, length):
  data = [int(x) for x in input().strip().split()]
  minutes = (data[0] * 60) + data[1]
  print(1440 - minutes)