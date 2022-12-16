myfile = open("input.txt")
content = myfile.read()
content = content.split()[0]

floor = 0
for i, char in enumerate(list(content)):
  if char == "(":
    floor += 1
  else:
    floor -= 1
  if floor == -1:
    print(i+1)
    break
