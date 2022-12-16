#Started 17/02/2021 15:10
#Ended 22/02/2021 13:58

myfile = open("input.txt")
content = myfile.read()

#Parsing Content
import re
import numpy as np
coordinates = np.array([[int(re.search('(\d+),', line)[1]), int(re.search(', (\d+)', line)[1])] for line in content.splitlines()]) + 1

#Make the size of the grid, the largest coordinates
grid_size = [min(coordinates[:,0]), min(coordinates[:,1]), max(coordinates[:,0]), max(coordinates[:,1])]
coordinate_areas = np.zeros(len(coordinates))

def calculate_distance(xy1, xy2):
	return abs(xy1[0]-xy2[0]) + abs(xy1[1]-xy2[1])
	
for x in range(grid_size[0], grid_size[2]+1):
	for y in range(grid_size[1], grid_size[3]+1):
		distances = np.array([calculate_distance(coordinate, [x,y]) for coordinate in coordinates])
		if sum(min(distances)==distances)==1:
			if x in [grid_size[0], grid_size[2]] or y in [grid_size[1], grid_size[3]]:
				coordinate_areas[distances.argmin()] = -1
			else:
				coordinate_areas[distances.argmin()] += 1

print(max(coordinate_areas))
