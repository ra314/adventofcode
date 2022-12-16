myfile = open("input2.txt")
content = myfile.read()

#{{<ab>},{<ab>},{<ab>},{<ab>}}

group_level = 0
score = 0
in_garbage = False
skip = False
amount_of_garbage = 0

for char in content:
  if skip:
    skip = False
    continue
  
  if not in_garbage:
    if char == "{":
      group_level += 1
      score += group_level
    elif char == "}":
      group_level -= 1
    elif char == "<":
      in_garbage = True
  else:
    if char == "!":
      skip = True
    elif char == ">":
      in_garbage = False
    else:
      amount_of_garbage += 1

print(amount_of_garbage)

