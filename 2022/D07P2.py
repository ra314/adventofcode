import re
myfile = open("input2.txt")
content = myfile.read()

class File:
  def __init__(self, name, size, is_file, parent_file):
    self.name = name
    self.size = size
    self.is_file = is_file
    self.parent_file = parent_file
    self.children = {}

root = File("/", 0, False, None)
all_filees = []
curr = root
i = 1
content = content.splitlines()
while i < len(content):
  if content[i].split()[-1] == "ls":
    i += 1
    while content[i][0] != "$":
      file_or_dir_name = content[i].split()[-1]
      if content[i].split()[0] == "dir":
        folder = File(file_or_dir_name, 0, False, curr)
        all_filees.append(folder)
        curr.children[file_or_dir_name] = folder
      elif content[i].split()[0].isdigit():
        file_size = int(content[i].split()[0])
        filee = File(file_or_dir_name, file_size, True, curr)
        all_filees.append(filee)
        curr.children[file_or_dir_name] = filee
      else:
        assert(False)
      i += 1
      if i >= len(content):
        break
  elif content[i].split()[-1] == "..":
    curr = curr.parent_file
    i += 1
  elif content[i].split()[1] == "cd" and content[i].split()[-1].isalpha():
    curr = curr.children[content[i].split()[-1]]
    i += 1

def get_size(filee):
  total = 0
  if filee.is_file:
    total += filee.size
  else:
    for child in filee.children.values():
      total += get_size(child)
  return total

dir_sizes = []
for filee in all_filees:
  if filee.is_file:
    continue
  dir_sizes.append((filee.name, get_size(filee)))

req_space = 30000000 - (70000000-get_size(root))
dir_sizes = list(filter(lambda x: x[1]>=req_space, dir_sizes))
dir_sizes = sorted(dir_sizes, key=lambda x: x[1])
print(dir_sizes[0])
