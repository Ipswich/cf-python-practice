length = int(input())

tallies = {
  "mishka": 0,
  "chris": 0
}
for index in range(0, length):
  mishka, chris = [int(x) for x in input().strip().split()]

  if mishka > chris:
    tallies["mishka"] += 1
  elif chris > mishka:
    tallies["chris"] += 1

if tallies["mishka"] > tallies["chris"]:
  print("Mishka")
elif tallies["chris"] > tallies["mishka"]:
  print("Chris")
else: 
  print("Friendship is magic!^^")
