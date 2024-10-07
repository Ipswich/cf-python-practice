length = int(input())

word = "codeforces"

for index in range(0, length):
  diff = 0
  new_word = input()

  for index in range(0, len(new_word)):
    if (new_word[index] != word[index]):
      diff += 1

  print(diff)