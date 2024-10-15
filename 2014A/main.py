test_count = int(input())

for test in range(test_count):
  n, k = [int(x) for x in input().strip().split()]
  a = [int(x) for x in input().strip().split()]
  g = 0
  p = 0
  for i in a:
    if i >= k:
      g += i
    elif i == 0 and g > 0:
      g -= 1
      p += 1

  print(p)