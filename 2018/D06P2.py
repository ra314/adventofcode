#Started 22/02/2021 13:58
#Ended 22/02/2021 14:24

myfile = open("input.txt")
content = myfile.read()

#Parsing Content
import re
import numpy as np
coordinates = np.array([[int(re.search('(\d+),', line)[1]), int(re.search(', (\d+)', line)[1])] for line in content.splitlines()]) + 1

#Make the size of the grid, the largest coordinates
grid_size = [min(coordinates[:,0]), min(coordinates[:,1]), max(coordinates[:,0]), max(coordinates[:,1])]
points_in_region = 0

def calculate_distance(xy1, xy2):
	return abs(xy1[0]-xy2[0]) + abs(xy1[1]-xy2[1])

all_points = []
for x in range(grid_size[0], grid_size[2]+1):
	for y in range(grid_size[1], grid_size[3]+1):
		all_points.append([x,y])

def distance_sum_to_coordinates(xy):
	return sum([calculate_distance(coordinate, xy) for coordinate in coordinates])

from multiprocessing import Pool
p = Pool(8)
output = p.map(distance_sum_to_coordinates, all_points)
print(sum(np.array(output)<10000))
#Wow didn't even have to check points outside the region
