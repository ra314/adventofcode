myfile = open("input.txt")
content = myfile.read()

count = 0
for line in content.splitlines():
  if len(line.split()) == len(set(line.split())):
    count += 1

print(count)
