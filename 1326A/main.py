tests = int(input())


for i in range(0, tests):
  integer = int(input())
  if integer == 1:
    print(-1)
  else:
    val = "5"
    for j in range(1, integer):
      val += "7"
    print(val)