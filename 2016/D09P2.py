import re

content = open("input.txt").read().strip()

def get_len(string):
  print(string)
  i = 0
  char_counter = 0
  while i < len(string):
    if string[i] == "(":
      match_obj = re.search(r'\((\d+)x(\d+)\)', string[i:])
      match = match_obj[0]
      num1 = int(match_obj[1])
      num2 = int(match_obj[2])
      i += len(match)
      print(string, i, match, num1, num2)
      char_counter += (num2 * get_len(string[i:][:num1]))
      i += num1
    else:
      i += 1
      char_counter += 1
  return char_counter

print(get_len("(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN"))
print(get_len(content))
