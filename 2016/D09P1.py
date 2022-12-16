import re

content = open("input.txt").read().strip()

i = 0
char_counter = 0
while i < len(content):
  print(content[i])
  if content[i] == "(":
    match_obj = re.search(r'\((\d+)x(\d+)\)', content[i:])
    match = match_obj[0]
    num1 = int(match_obj[1])
    num2 = int(match_obj[2])
    i += len(match)
    i += num1
    char_counter += num1*num2
  else:
    i += 1
    char_counter += 1
  print(i, char_counter)
