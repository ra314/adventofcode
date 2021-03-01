myfile = open("input.txt")
content = myfile.read()
content = content.splitlines()

size = len(content)
import numpy as np
seed = np.zeros((size, size))

#This is the initial 2d slice state
for i in range(size):
	for j in range(size):
		if content[i][j] == '#':
			seed[i][j] = 1
			
#This function finds the number of adjacent active boxes
import itertools
alterations = list(itertools.product([-1,0,1], repeat=3))
alterations.remove((0,0,0))

def adjacent_active_count(x,y,z):
	orig_coordinates = np.array([x,y,z])
	count = 0
	for alteration in alterations:
		curr_coordinates = orig_coordinates + alteration
		if not (0 <= curr_coordinates[0] < sizes[0]): continue
		if not (0 <= curr_coordinates[1] < sizes[1]): continue
		if not (0 <= curr_coordinates[2] < sizes[2]): continue
		count += prev_world[curr_coordinates[0],curr_coordinates[1],curr_coordinates[2]]
	return count
	
#Prints the world by z slices
def print_world(world):
	for z in range(np.shape(world)[2]):
		print(f"z={z}")
		print(world[:,:,z])

#This is the size of the world we are considering
sizes = np.array([size+2, size+2, 3])
prev_world = np.zeros((sizes[0], sizes[1], sizes[2]))
prev_world[1:(sizes[0]-1),1:(sizes[1]-1),1] = seed

for i in range(6):
	curr_world = np.copy(prev_world)
	
	for x in range(sizes[0]):
		for y in range(sizes[1]):
			for z in range(sizes[2]):
				count = adjacent_active_count(x,y,z)
				if prev_world[x,y,z] == 1:
					if count not in [2,3]: curr_world[x,y,z] = 0
				else:
					if count == 3: curr_world[x,y,z] = 1
	
	#This is the number of active cubes
	print(np.sum(curr_world))
	#print_world(curr_world)
	sizes += 2
	prev_world = np.zeros((sizes[0], sizes[1], sizes[2]))
	prev_world[1:(sizes[0]-1),1:(sizes[1]-1),1:(sizes[2]-1)] = curr_world
