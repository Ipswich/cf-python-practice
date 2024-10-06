import sys

implement = 0
for line in sys.stdin:
  numbers = [int(x) for x in line.strip().split()]
  ones = [x for x in numbers if x == 1]

  if len(ones) > 1:
    implement += 1

print(implement)