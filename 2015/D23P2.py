myfile = open("input2.txt")
content = myfile.read()
content = content.splitlines()

reg = {'a':1, 'b':0}
i = 0

while i<len(content):
  print(reg, i)
  line = content[i].split()
  if line[0] == "inc":
    reg[line[1]] += 1
  elif line[0] == "tpl":
    reg[line[1]] *= 3
  elif line[0] == "hlf":
    reg[line[1]] //= 2
  elif line[0] == "jmp":
    i += int(line[1])
    continue
  elif line[0] == "jio":
    if reg[line[1][:-1]] == 1:
      i += int(line[2])
      continue
  elif line[0] == "jie":
    if reg[line[1][:-1]]%2 == 0:
      i += int(line[2])
      continue
  i+=1

print(reg['b'])
