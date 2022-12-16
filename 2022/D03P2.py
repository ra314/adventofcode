myfile = open("input.txt")
content = myfile.read()

lines = content.splitlines()
total = 0
while lines:
  a, b, c = lines.pop(), lines.pop(), lines.pop()
  print(a,b,c)
  a, b, c = set(a), set(b), set(c)
  inter = a.intersection(b).intersection(c)
  assert(len(inter)==1)
  inter = list(inter)[0]
  if inter.isupper():
    total += ord(inter)-ord("A")+27
  else:
    total += ord(inter)-ord("a")+1

print(total)
