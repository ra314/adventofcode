#Started 23/02/2021 23:19
#Ended 24/02/2021 00:43

myfile = open("input.txt")
content = myfile.read()

grid = [list(line) for line in content.splitlines()]

import numpy as np
move_vectors = {}
move_vectors['^'] = np.array([0,-1])
move_vectors['<'] = np.array([-1,0])
move_vectors['>'] = np.array([1,0])
move_vectors['v'] = np.array([0,1])

class Cart:
	def __init__(self, xy, icon):
		self.xy = np.array(xy)
		self.icon = icon
		self.times_turned = 0
		
	def move(self):
		self.track = grid[self.xy[1]][self.xy[0]]
		
		if self.track == '\\':
			if self.icon in '^v':
				self.rotate_left(1)
			elif self.icon in '<>':
				self.rotate_left(3)
				
		elif self.track == '/':
			if self.icon in '^v':
				self.rotate_left(3)
			elif self.icon in '<>':
				self.rotate_left(1)
				
		elif self.track == '+':
			self.change_direction()
			
		elif self.track == '-|':
			pass
				
		self.xy += move_vectors[self.icon]
		
	def rotate_left(self, times):
		while times != 0:
			if self.icon == '^':
				self.icon = '<'
			elif self.icon == '<':
				self.icon = 'v'
			elif self.icon == 'v':
				self.icon = '>'
			elif self.icon == '>':
				self.icon = '^'
			times -= 1
		
	def change_direction(self):
		self.times_turned = (self.times_turned + 1) % 3
		if self.times_turned == 1:
			self.rotate_left(1)
		elif self.times_turned == 2:
			return
		elif self.times_turned == 0:
			self.rotate_left(3)

#Finding the carts, removing them from the grid, replacing them with tracks
#and creating a list of cart objects
carts = []
for y in range(len(grid)):
	for x in range(len(grid[0])):
		if grid[y][x] in '<>^v':
			carts.append(Cart([x,y],grid[y][x]))
			if grid[y][x] in '<>':
				grid[y][x] = '-'
			elif grid[y][x] in '^v':
				grid[y][x] = '|'

def print_grid():
	removed_tracks = []
	for cart in carts:
		removed_tracks.append(grid[cart.xy[1]][cart.xy[0]])
		grid[cart.xy[1]][cart.xy[0]] = cart.icon
		
	for line in grid:
		print(''.join(line))
		
	for cart in carts:
		grid[cart.xy[1]][cart.xy[0]] = removed_tracks.pop(0)
		
	print()
	
def detect_collision():
	coordinates = []
	for cart in carts:
		xy = list(cart.xy)
		if xy in coordinates:
			cart.icon = 'X'
			carts[coordinates.index(xy)].icon = 'X'
			return xy
		else:
			coordinates.append(xy)
	return False
	
		
def simulate_tick():
	for cart in carts:
		cart.move()
	coordinates = detect_collision()
	#print_grid()
	if coordinates != False:
		print(coordinates)
		return False
	return True
	
#print_grid()
while simulate_tick():
	pass
