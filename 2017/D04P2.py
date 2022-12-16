myfile = open("input2.txt")
content = myfile.read()

count = 0
for line in content.splitlines():
  words = []
  for word in line.split():
    words.append("".join(sorted(word)))
  if len(words) == len(set(words)):
    count += 1

print(count)
