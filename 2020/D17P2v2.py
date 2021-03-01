##v2 includes code for parellisation

myfile = open("input2.txt")
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
alterations = list(itertools.product([-1,0,1], repeat=4))
alterations.remove((0,0,0,0))
	
def adjacent_active_count(coordinates):
	coordinates = np.array(coordinates)
	count = 0
	skip = False
	for alteration in alterations:
		adjacent = coordinates + alteration
		if not np.all(np.logical_and((np.zeros(4) <= adjacent), (adjacent < sizes))): continue
		#print(adjacent, prev_world[tuple(adjacent)])
		count += prev_world[tuple(adjacent)]
	return count
	
#Prints the world by z&w slices
def print_world(world):
	for z in range(np.shape(world)[2]):
		for w in range(np.shape(world)[3]):
			print(f"z={z}, w={w}")
			print(world[:,:,z,w])

#This is the size of the world we are considering
sizes = np.array([size+2, size+2, 3, 3])
prev_world = np.zeros((sizes[0], sizes[1], sizes[2], sizes[3]))
prev_world[1:(sizes[0]-1),1:(sizes[1]-1),1,1] = seed
curr_world = np.copy(prev_world)

#Multithreading
from multiprocessing import Pool
#This function returns the given coordinate and the number
#It should be changed to, if it should be changed
def update_world(coordinates):
	count = adjacent_active_count(coordinates)
	if prev_world[tuple(coordinates)] == 1:
		if count not in [2,3]:
			return coordinates, 0 
	else:
		if count == 3: 
			return coordinates, 1

import time
start = time.time()
for i in range(3):	
	#These are the possible values provided to perform the cartesian
	#product and get all the coordinates of the world
	possible_values = []
	for size in sizes: possible_values.append(list(range(size)))
	inputs = list(itertools.product(*possible_values))
	p = Pool(8)
	output = p.map(update_world, inputs)
	p.close()
	p.join()
	
	#Change the state of the cubes
	output = list(filter(None, output))
	for coordinate, value in output:
		curr_world[coordinate] = value
	
	#This is the number of active cubes
	print(np.sum(curr_world))
	#print_world(curr_world)
	sizes += 2
	prev_world = np.zeros((sizes[0], sizes[1], sizes[2], sizes[3]))
	prev_world[1:(sizes[0]-1),1:(sizes[1]-1),1:(sizes[2]-1),1:(sizes[3]-1)] = curr_world
	curr_world = np.copy(prev_world)
	
print(time.time()-start)

#35.55 seconds for 6 iterations on the small 3by3 input
#2.66 seconds for 3 iterations on the small 3by3 input
