myfile = open("input.txt")
content = myfile.read()

total = 0
for line in content.splitlines(): 
  a, b = line[len(line)//2:], line[:len(line)//2]
  a, b = set(a), set(b)
  inter = list(a.intersection(b))
  assert(len(inter)) == 1
  inter = inter[0]
  if inter.isupper():
    total += ord(inter)-ord("A")+27
  else:
    total += ord(inter)-ord("a")+1

print(total)

