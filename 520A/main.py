import sys

alphabet = "abcdefghijklmnopqrstuvwxyz"
length = int(input())

line = input().lower()
for char in line:
  try:
    alphabet = alphabet.replace(char, "")
  except:
    pass

if len(alphabet) > 0:
  print("NO")
else:
  print("YES")
