myfile = open("input2.txt")
content = myfile.read()

from collections import defaultdict
replacements = defaultdict(list)
for line in content.splitlines():
  if line == "": break
  line = line.split()
  replacements[line[0]].append(line[2])

medicine_molecule = content.splitlines()[-1]
distinct_molecules = set()

i = 0
while i<len(medicine_molecule):
  char = medicine_molecule[i]
  char2 = medicine_molecule[i:i+2]
  if char in replacements:
    for replacement in replacements[char]:
      distinct_molecules.add(medicine_molecule[:i] + replacement + medicine_molecule[i+1:])
  if char2 in replacements:
    for replacement in replacements[char2]:
      distinct_molecules.add(medicine_molecule[:i] + replacement + medicine_molecule[i+2:])
  i += 1

#print(distinct_molecules)
print(len(distinct_molecules))
