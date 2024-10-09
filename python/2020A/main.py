test_count = int(input())

for test in range(test_count):
  n, k = [int(x) for x in input().strip().split()]
  moves = 0
  if k == 1:
    moves = n
  else:
    while n:
      moves += n % k
      n //= k
  
  print(moves)