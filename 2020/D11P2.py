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
			curr_cell_index = [i,j]
			curr_cell = prev_state[i][j]
			adjacent_cells = find_adjacent_cells(curr_cell_index, prev_state)
			if curr_cell == 'L':
				if '#' not in "".join(adjacent_cells):
					next_state[i][j] = '#'
			elif curr_cell == '#':
				if "".join(adjacent_cells).count('#') >= 5:
					next_state[i][j] = 'L'
	return next_state
	
def find_adjacent_cells(curr_cell_index, prev_state):
	adjacent_cells = []
	for modifier in adjacent_modifier:
		curr_adjacent_index = modifier + curr_cell_index
		while (0 <= curr_adjacent_index[0] < height) and (0 <= curr_adjacent_index[1] < width):
				curr_adjacent = prev_state[curr_adjacent_index[0]][curr_adjacent_index[1]]
				if curr_adjacent == '.':
					curr_adjacent_index += modifier
				else:
					adjacent_cells.append(curr_adjacent)
					break
	return adjacent_cells
	
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
