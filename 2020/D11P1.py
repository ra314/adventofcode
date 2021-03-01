import numpy as np
import copy

myfile = open("input.txt")
content = myfile.read()
prev_state = [list(line) for line in content.split()]
height = len(prev_state)
width = len(prev_state[0])
adjacent_modifier = np.array([[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]])

def update_state(prev_state):
	next_state = copy.deepcopy(prev_state)
	for i in range(height):
		for j in range(width):
			adjacent_indexes = [i,j] + adjacent_modifier
			adjacent_cells = []
			curr_cell = prev_state[i][j]
			for index in adjacent_indexes:
				if (0 <= index[0] < height) and (0 <= index[1] < width):
					adjacent_cells.append(prev_state[index[0]][index[1]])
			if curr_cell == 'L':
				if '#' not in "".join(adjacent_cells):
					next_state[i][j] = '#'
			elif curr_cell == '#':
				if "".join(adjacent_cells).count('#') >= 4:
					next_state[i][j] = 'L'
	return next_state
	
def print_seats(array):
	for line in next_state:
		print("".join(line))
	print()

next_state = update_state(prev_state)
print_seats(next_state)
while prev_state != next_state:
	prev_state = next_state
	next_state = update_state(prev_state)
	print_seats(next_state)

def flatten(array):
	output = ""
	for x in array:
		for y in x:
			output += y
	return output
	
seats_occupied = flatten(next_state).count('#')
print(seats_occupied)
