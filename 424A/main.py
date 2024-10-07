hamster_count = int(input())
half_hamster_count = hamster_count / 2
hamster_pose = input()

currently_standing_hamsters = hamster_pose.count("X")

minutes = 0
while(currently_standing_hamsters != half_hamster_count):
  minutes += 1
  if (currently_standing_hamsters > half_hamster_count):
    hamster_pose = hamster_pose.replace("X", "x", 1)
  else:
    hamster_pose = hamster_pose.replace("x", "X", 1)
  currently_standing_hamsters = hamster_pose.count("X")

print(minutes)
print(hamster_pose)