import re
myfile = open("input.txt")
content = myfile.read().splitlines()

def snaf_to_num(line):
  num = 0
  for i, char in enumerate(line[::-1]):
    if char == "=":
      char = "-2"
    if char == "-":
      char = "-1"
    digit = int(char)
    num += (digit*(5**(i)))
  return num

from math import inf

def num_to_snaf(num, guess):
  guess = list(guess)
  curr = snaf_to_num("".join(guess))
  i = 0
  while i+1 < len(guess):
    min_diff, min_char = inf, "X"
    for char in "210-=":
      guess[i+1] = char
      curr = snaf_to_num("".join(guess))
      diff = abs(curr-num)
      if diff < min_diff:
        min_diff, min_char = diff, char
    guess[i+1] = min_char
    i += 1
  return "".join(guess)

nums = []
for line in content:
  nums.append(snaf_to_num(line))

print(nums)
print(sum(nums))

print(32528703778465-snaf_to_num("20000000000000000000"))
print(num_to_snaf(32528703778465, "20000000000000000000"))
