myfile = open("input2.txt")
content = myfile.read()

graph = [[]] * len(content.splitlines())

for line in content.splitlines():
  graph[int(line.split()[0])] = list(map(int, line.split("<->")[-1].split(',')))

children = []

def get_children(index):
  for child in graph[index]:
    if child in children:
      continue
    else:
      children.append(child)
    get_children(child)
  return
  
get_children(0)
print(len(children))
