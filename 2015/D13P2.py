myfile = open("input2.txt")
content = myfile.read()

# Structure of dictionary
# {Alice : {Bob:+54, Carol:+79},
# {Bob : ...
happiness_dict = {}
curr_person = "Alice"
people = ["Alice"]
new_dict = {}
for line in content.splitlines():
  line = line.split()  
  if curr_person != line[0]:
      happiness_dict[curr_person] = new_dict
      new_dict = {}
      curr_person = line[0]
      people.append(curr_person)
  
  if line[2] == "gain":
    new_dict[line[-1][:-1]] = int(line[3])
  else:
    new_dict[line[-1][:-1]] = -int(line[3])
happiness_dict[curr_person] = new_dict

for person in people:
  happiness_dict[person]["Rahul"] = 0
new_dict = {}
for person in people:
  new_dict[person] = 0
happiness_dict["Rahul"] = new_dict
people.append("Rahul")

def evaluate(perm):
  happiness = 0
  for i, person in enumerate(perm):
    happiness += happiness_dict[person][perm[(i+1)%len(people)]]
    happiness += happiness_dict[person][perm[(i-1)%len(people)]]
  return happiness

import itertools
max_hap = 0
for perm in list(itertools.permutations(people)):
  max_hap = max(evaluate(perm), max_hap)
print(max_hap)
