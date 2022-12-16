myfile = open("input.txt")
content = myfile.read()

grid_serial_number = int(content)

import numpy as np
grid = np.zeros([300+1,300+1])

def calculate_power(x,y):
	rack_id = x + 10
	power_level = rack_id * y
	power_level += grid_serial_number
	power_level *= rack_id
	power_level = int(str(int(power_level/100))[-1])
	power_level -= 5
	return power_level

#Calculating powers
for i in range(len(grid)):
	for j in range(len(grid)):
		grid[i,j] = calculate_power(i,j)
		
#Calculating summed area table
#https://en.wikipedia.org/wiki/Summed-area_table
summed_area_grid = grid.copy()
sag = summed_area_grid
summed_area_grid[1,1] = grid[1,1]
for i in range(len(grid)):
	for j in range(len(grid)):
		if 0 in [i,j]:
			continue
		if [i,j] == [1,1]:
			continue
		if i != 1:
			summed_area_grid[i,j] += summed_area_grid[i-1,j]
		summed_area_grid[i,j] += sum(grid[i,1:j])
		
def calculate_square_power(x,y,l):
	return sag[x+l,y+l] - sag[x+l,y] - sag[x,y+l] + sag[x,y]

#Finding the are with most power
data = []
for l in range(1,300):
	for x in range(len(grid)-l):
		for y in range(len(grid)-l):
			data.append([x,y,l])

from multiprocessing import Pool	
import time
start = time.time()
p = Pool(16)
output = p.starmap(calculate_square_power, data)
print(time.time()-start)
print(np.array(data[np.argmax(output)]) + [1,1,0])
