test_count = int(input())

for test in range(test_count):
  n = int(input())
  x, y = [int(x) for x in input().strip().split()]

  limiter = x if x < y else y

  blend_cycles = -(n // -limiter)

  print(blend_cycles)