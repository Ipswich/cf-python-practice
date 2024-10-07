length = int(input())

for index in range(0, length):
  num_boxes = int(input())
  current_state = input()
  desired_state = input()

  cats_removed = 0
  cats_added = 0
  for box in range(0, num_boxes):
    if current_state[box] == desired_state[box]:
      continue
    if current_state[box] == "1" and desired_state[box] == "0":
      cats_removed += 1
    if current_state[box] == "0" and desired_state[box] == "1":
      cats_added +=1

  moves = 0
  while cats_removed != 0 and cats_added != 0:
    moves +=1
    cats_removed -= 1
    cats_added -= 1
  
  print(abs(moves + cats_removed + cats_added))
