can_count = int(input())
volumes_of_cola = [int(x) for x in input().strip().split()]
can_volumes = [int(x) for x in input().strip().split()]

largest = -1
second_largest = -2

for can in can_volumes:
  if can > largest:
    second_largest = largest
    largest = can
  elif can > second_largest:
    second_largest = can

total_volume = sum(volumes_of_cola)
if total_volume - largest - second_largest > 0:
  print("NO")
else:
  print("YES")