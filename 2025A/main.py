t = int(input())

for test in range(t):
  s = input()
  t = input()
  
  s_index = 0
  t_index = 0

  time = 0

  # matching start characters
  while s[s_index] == t[t_index]:
    time += 1
    s_index += 1
    t_index += 1
    if (s_index >= len(s) or t_index >= len(t)):
      break
  
  # Copy
  if time > 0:
    time += 1

  # Remaining characters
  time += (len(s) - s_index)
  time += (len(t) - t_index)
  print(time)