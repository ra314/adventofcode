import numpy as np

myfile = open("input2.txt")
content = myfile.read()
content = content.splitlines()
slope = np.array([1,3])
curr_coordinates = np.array([0,0])
num_trees = 0

while True:
	curr_coordinates += slope
	if curr_coordinates[0] >= len(content):
		break
	
	if content[curr_coordinates[0]][curr_coordinates[1]%len(content[0])] == '#':
		num_trees += 1
		
print(num_trees)
