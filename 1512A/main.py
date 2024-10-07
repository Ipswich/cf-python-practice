length = int(input())

for index in range(0, length):
  size = int(input())

  spy_list = [int(x) for x in input().strip().split()]

  indices = {}
  count = {}

  for index, element in enumerate(spy_list):
    if (count.get(element)):
      count[element] += 1
    else:
      count[element] = 1

    indices[element] = index

  keys = list(count.keys())

  element = -1
  if count[keys[0]] > count[keys[1]]:
    element = keys[1]
  else:
    element = keys[0]

  print(indices.get(element) + 1)
