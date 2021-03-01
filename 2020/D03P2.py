import numpy as np

myfile = open("input.txt")
content = myfile.read()
content = content.splitlines()
slopes = np.array([[1,1],[1,3],[1,5],[1,7],[2,1]])
curr_coordinates = np.array([0,0])
num_trees = 0
product = 1

for slope in slopes:
	while True:
		curr_coordinates += slope
		if curr_coordinates[0] >= len(content):
			break
		
		if content[curr_coordinates[0]][curr_coordinates[1]%len(content[0])] == '#':
			num_trees += 1
			
	curr_coordinates = np.array([0,0])
	product *= num_trees
	num_trees = 0

print("Number of Trees:", num_trees)
print("Product:", product)
