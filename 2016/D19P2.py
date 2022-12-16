myfile = open("input2.txt")
content = 3005290
#content = 5

num_elves = content
elves = list(range(1,num_elves+1))

index = 0
while len(elves) > 2:
  del elves[(index + len(elves)//2)%len(elves)]
  index += 1
  if len(elves)%1000 == 0:
    print(len(elves))

print(elves)
