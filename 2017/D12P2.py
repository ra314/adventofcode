myfile = open("input2.txt")
content = myfile.read()

graph = [[]] * len(content.splitlines())

for line in content.splitlines():
  graph[int(line.split()[0])] = list(map(int, line.split("<->")[-1].split(',')))

def get_children(index):
  for child in graph[index]:
    if child in children:
      continue
    else:
      children.append(child)
    get_children(child)
  return

all_children = set()
for index in range(len(graph)):
  children = []
  get_children(index)
  all_children.add("".join(map(str, sorted(children))))
print(len(all_children))
