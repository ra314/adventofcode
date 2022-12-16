#Started 23/02/2021 11:54
#Ended 23/02/2021 12:29

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
		
#Finding area with most power
highest_power = -100
coordinates_of_highest_power = [0,0]
for i in range(len(grid)-3):
	for j in range(len(grid)-3):
		curr_power = sum(sum(grid[i:i+3,j:j+3]))
		if curr_power > highest_power:
			highest_power = curr_power
			coordinates_of_highest_power = [i,j]
