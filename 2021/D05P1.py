import numpy as np
myfile = open("input.txt")
content = myfile.read()

coords = []
for line in content.splitlines():
    line_segment = []
    for coord_pair in line.split(' -> '):
        line_segment.append(list(map(int, coord_pair.split(','))))
    coords.append(line_segment)

size = np.array(coords).max()+2
floor_map = np.zeros((size, size))

for coord_pair in coords:
    if (coord_pair[0][0] == coord_pair[1][0]):
        x = [coord_pair[0][1], coord_pair[1][1]]
        floor_map[coord_pair[0][0],min(x):max(x)+1] += 1 
    elif (coord_pair[0][1] == coord_pair[1][1]):
        x = [coord_pair[0][0], coord_pair[1][0]]
        floor_map[min(x):max(x)+1,coord_pair[0][1]] += 1 
    else:
        continue

print((floor_map>1).sum())
