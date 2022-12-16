myfile = open("input.txt")
content = myfile.read()

visited_houses = set([(0,0)])
def visit_houses(content):
  curr_location = (0,0)
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

visit_houses(content[1::2])
visit_houses(content[::2])

print(len(visited_houses))
