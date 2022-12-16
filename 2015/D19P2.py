import re
from llist import dllist, dllistnode
from collections import defaultdict
import math

myfile = open("input.txt")
content = myfile.read()

def get_molecules(string):
  return re.findall(r'([A-Z][a-z]*)\1*', string)

replacements = defaultdict(list)
for line in content.splitlines():
  if line == "": break
  line = line.split()
  # >>> re.findall(r'([A-Z][a-z]*)\1*', "ThRnFAr")
  # ['Th', 'Rn', 'F', 'Ar']
  replacements[line[0]].append(get_molecules(line[2]))

medicine_molecule = get_molecules(content.splitlines()[-1])

# BFS that terminates when you hit the length of the target
def curse(molecules, target, depth):
  if molecules.size > len(target):
    return -1
  if list(molecules.itervalues()) == target:
    return depth
  depth += 1
  for node in molecules.iternodes():
    if node.value not in replacements:
      continue
    for replacement in replacements[node.value]:
      # Insert replacements
      curr = node
      for new_mol in replacement:
        curr = molecules.insertafter(new_mol, curr)
      molecules.remove(node)
      # Perform recursion
      val = curse(molecules, target, depth)
      if val != -1:
        return val
      # Remove replacements
      for i in range(len(replacement)):
        curr, _ = curr.prev, molecules.remove(curr)
      molecules.insertafter(node.value, curr)
  return -1

def curse_2(molecules, target, depth, curr_best):
  if len(molecules) > len(target):
    return math.inf
  if molecules == target:
    return min(depth, curr_best)
  for i, mol in enumerate(molecules):
    if mol not in replacements:
      continue
    for replacement in replacements[mol]:
      # Perform recursion
      val = curse_2(molecules[:i] + replacement + molecules[i+1:], target, depth+1, curr_best)
      curr_best = min(val, curr_best)
  return curr_best

#curse(dllist(['e']), medicine_molecule, 0)
print(curse_2(['e'], medicine_molecule, 0, math.inf))