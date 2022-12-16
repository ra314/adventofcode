myfile = open("input2.txt")
content = myfile.read()

curr_location = (0,0)
visited_houses = set([curr_location])
for char in content:
  if char == "^":
    curr_location = (curr_location[0], curr_location[1]+1)
  elif char == "v":
    curr_location = (curr_location[0], curr_location[1]-1)
  elif char == "<":
    curr_location = (curr_location[0]+1, curr_location[1])
  elif char == ">":
    curr_location = (curr_location[0]-1, curr_location[1])
  visited_houses.add(curr_location)

print(len(visited_houses))
