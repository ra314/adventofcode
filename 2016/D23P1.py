myfile = open("input2.txt")
content = myfile.read()

register = {}
register['a'] = 7
index = 0
lines = [line.split() for line in content.splitlines()]

while index < len(lines):
  line = lines[index]
  print(index, line)
  
  if line[1].isdigit() or ("-" in line[1]):
    value1 = int(line[1])
  else:
    value1 = register[line[1]]
  if len(line) == 3:
    if line[2].isdigit() or ("-" in line[2]):
      value2 = int(line[2])
    elif line[2] in register:
      value2 = register[line[2]]
    else:
      value2 = "boop"
  
  if line[0] == "cpy":
    if not line[2].isdigit():
        register[line[2]] = value1
  elif line[0] == "tgl":
    target_line_index = index + value1
    if target_line_index in range(len(lines)):
      target_line = lines[target_line_index]
      if len(target_line) == 2:
        if target_line[0] == "inc":
          target_line[0] = "dec"
        else:
          target_line[0] = "inc"
      elif len(target_line) == 3:
        if target_line[0] == "jnz":
          target_line[0] = "cpy"
        else:
          target_line[0] = "jnz"
  elif line[0] in ["inc", "dec"]:
    if not line[1].isdigit():
      if line[0] == "inc":
        register[line[1]] += 1
      else:
        register[line[1]] -= 1
  elif line[0] == "jnz":
    if value1 != 0:
      index += value2
      continue
  index += 1

print(register)
