myfile = open("input2.txt")
content = myfile.read()

dic = {}
for line in content.splitlines():
  if "->" in line:
    children = line.split('->')[1].split()
    children[-1] = children[-1] + ','
    for i in range(len(children)):
      children[i] = children[i][:-1]
    dic[line.split()[0]] = children
  else:
    dic[line.split()[0]] = []

def find_num_children(name):
  if dic[name] == []:
    return 0
  else:
    retval = len(dic[name])
    for child_name in dic[name]:
      retval += find_num_children(child_name)
    return retval

max_name = ""
max_val = 0
for name in dic:
  val = find_num_children(name)
  if val > max_val:
    max_val = val
    max_name = name

print(max_name, max_val)
