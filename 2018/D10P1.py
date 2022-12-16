#Started 22/02/2021 23:15
#Ended 23/02/2021 00:50

myfile = open("input3.txt")
content = myfile.read()

#Parsing input
positions = []
velocities = []
import re
import numpy as np
for line in content.splitlines():
	nums = np.array([int(num) for num in re.findall('-?\d+', line)])
	positions.append([nums[0], nums[1]])
	velocities.append([nums[2], nums[3]])
positions = np.array(positions)
velocities = np.array(velocities)

def print_grid():
	global positions
	positions -= [min(positions[:,0]), min(positions[:,1])]
	grid_size = [max(positions[:,0])+1, max(positions[:,1])+1]
	grid = np.zeros(grid_size)
	for position in positions:
		grid[tuple(position)] = 1
	grid = np.rot90(grid, 3)
	grid = np.flip(grid, 1)
	chars = [['#' if num else '.' for num in line] for line in grid]
	strings = [''.join(line) for line in chars]
	for line in strings:
		print(line)
	
def calculate_clustering():
	return sum(sum(abs(([positions[0]]*len(positions)) - positions)))

prev_clustering = calculate_clustering()
reps = 100000
for i in range(reps):
	positions += velocities
	curr_clustering = calculate_clustering()
	if prev_clustering < curr_clustering:
		break
	else:
		prev_clustering = curr_clustering
	if curr_clustering < 10000:
		print_grid()

#24s without vectorization
#7.4s with vectorization
#scrub back and forward with positions += velocities or positions -= velocities
