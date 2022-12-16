myfile = open("input2.txt")
content = 3005290
#content = 5

num_elves = content
elves = list(range(1,num_elves+1))

while len(elves) > 1:
  if len(elves) % 2 == 0:
    del elves[1::2]
  else:
    del elves[1::2]
    del elves[0]

print(elves)
