length = int(input())

for index in range(0, length):
  a, b, c = [int(x) for x in input().strip().split()]

  if (a + b == c):
    print("+")
  else:
    print("-")