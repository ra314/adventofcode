#Started 23/02/2021 12:30
#Ended 23/02/2021 13:13

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

def calculate_square_power(x,y,l):
	return sum(sum(grid[x:x+l,y:y+l]))
	
#Finding area with most power
'''
highest_power = -100
coordinates_of_highest_power = [0,0,0]
for l in range(1,301):
	print(l)
	for x in range(len(grid)-l+1):
		for y in range(len(grid)-l+1):
			curr_power = calculate_square_power(x,y,l)
			if curr_power > highest_power:
				highest_power = curr_power
				coordinates_of_highest_power = [x,y,l]
'''
data = []
for l in range(1,301):
	for x in range(len(grid)-l+1):
		for y in range(len(grid)-l+1):
			data.append([x,y,l])

from multiprocessing import Pool	
import time
start = time.time()
p = Pool(16)
output = p.starmap(calculate_square_power, data)
print(time.time()-start)
print(data[np.argmax(output)])
