myfile = open("input3.txt")
content = myfile.read()

import numpy as np
import re

#Reads the input file and finds strings that refer to the tile number and the tile itself
def parse_tiles(content):
	tile_nums = re.findall('\d+', content)
	tiles = [np.array([list(line) for line in tile.split()]) for tile in re.findall('(?:[.#]+\n)+', content)]
	return zip(tile_nums, tiles)

class Tile:
	def __init__(self, tile_num, tile):
		self.tile_num = tile_num
		self.tile = tile
		self.generate_edges()
		self.neighbours = []
		self.coordinates = np.array([])
		self.location_fixed = False
		
	def generate_edges(self):
		tile = self.tile
		self.edges = [list(edge) for edge in [tile[0,:], tile[-1,:], tile[:,-1], tile[:,0]]]
		edges = self.edges
		self.dict_edges = {'N':edges[0], 'S':edges[1], 'E':edges[2], 'W':edges[3]}
		
	def flip(self, direction):
		if direction in 'NS':
			self.tile = self.tile[:,::-1]
		elif direction in 'EW':
			self.tile = self.tile[::-1,:]
		self.generate_edges()
		
	def rotate(self):
		self.tile = np.rot90(self.tile)
		self.generate_edges()
		
	def remove_edges(self):
		self.tile = self.tile[1:-1,1:-1]
		self.generate_edges()
		
#Converts all of the found tiles into Tile objects
tiles = {}
for tile_num, tile in parse_tiles(content):
	tiles[tile_num] = Tile(tile_num, tile)
	
#This function compares the edges between two tiles for a match
def are_neighbours(tile1, tile2):
	if tile1 in tile2.neighbours:
		return True
		
	for edge in tile1.edges:
		for i in range(len(tile2.edges)):
			if edge in [tile2.edges[i], tile2.edges[i][::-1]]:
				tile1.neighbours.append(tile2)
				tile2.neighbours.append(tile1)
				return True
	return False

import math
#This is the size of the image in tiles
grid_size = int(math.sqrt(len(tiles)))
grid = [[0]*((grid_size*2)-1)] * ((grid_size*2)-1)

#Iterating through tiles and finding all neighbours
for tile1 in tiles.values():
	for tile2 in tiles.values():
		if tile1.tile_num == tile2.tile_num:
			continue
		else:
			are_neighbours(tile1, tile2)

def print_all_neighbours():
	for tile in tiles.values():
		print(tile.tile_num, [neighbour.tile_num for neighbour in tile.neighbours])

import random		
seed_tile = random.choice(list(tiles.values()))
seed_tile.coordinates = np.array([0,0])
seed_tile.location_fixed = True
tiles_to_process = [seed_tile]

def find_relative_direction(tile1, tile2):
	for edge1, direction1 in zip(tile1.edges, ['N','S','E','W']):
		for edge2, direction2 in zip(tile2.edges, ['N','S','E','W']):
			if edge1 in [edge2, edge2[::-1]]:
				return direction1, direction2

def rotate(direction):
	if direction == 'N': return 'W'
	elif direction == 'W': return 'S'
	elif direction == 'S': return 'E'
	elif direction == 'E': return 'N'
	
def relative_coordinates(direction):
	if direction == 'N': return np.array([0,1])
	elif direction == 'W': return np.array([-1,0])
	elif direction == 'S': return np.array([0,-1])
	elif direction == 'E': return np.array([1,0])

def fix_location_of_neighbours(tile):
	for neighbour in tile.neighbours:
		if neighbour.location_fixed: continue
		
		direction1, direction2 = find_relative_direction(tile, neighbour)
		
		while direction1 + direction2 not in ['NS','SN','EW','WE']:
			neighbour.rotate()
			direction2 = rotate(direction2)
			
		if tile.dict_edges[direction1] != neighbour.dict_edges[direction2]:
			neighbour.flip(direction2)
			
		neighbour.coordinates = tile.coordinates + relative_coordinates(direction1)
		neighbour.location_fixed = True
		tiles_to_process.append(neighbour)
		
###Finding coordinates for all the tiles
for tile in tiles_to_process:
	fix_location_of_neighbours(tile)

###Removing Edges of Tiles
for tile in tiles.values():
	tile.remove_edges()

###Sorting the tiles
sorted_tiles = sorted(tiles.values(), key = lambda obj: [-obj.coordinates[1], obj.coordinates[0]])
tile_nums = [tile.tile_num for tile in sorted_tiles]

horizontal_slices = []
while sorted_tiles:
	horizontal_slice = [tile.tile for tile in sorted_tiles[:grid_size]]
	horizontal_slices.append(np.concatenate((horizontal_slice), axis = 1))
	del sorted_tiles[:grid_size]
big_tile = np.concatenate((horizontal_slices),axis=0)

tile_nums_arranged = []
while tile_nums:
	tile_nums_arranged.append(tile_nums[:grid_size])
	del tile_nums[:grid_size]

###Finding the monster
monster = "                  # \n#    ##    ##    ###\n #  #  #  #  #  #   \n"
pattern = "(?=[.#]{13}#[.#](?=[.#]{0,76}![.#]{0,76}).{77}#....##....##....###(?=[.#]{0,76}![.#]{0,76}).{77}.#..#..#..#..#..#)"
#pattern = "(?=[.#]{13}#[.#].{77}#....##....##....###.{77}.#..#..#..#..#..#)"


###Creating permutations of the big tile by rotating and flipping
big_tile_permutations = []
big_tile_permutations.extend([big_tile, np.rot90(big_tile,1), np.rot90(big_tile,2), np.rot90(big_tile,3)])
big_tile = big_tile[::-1,:]
big_tile_permutations.extend([big_tile, np.rot90(big_tile,1), np.rot90(big_tile,2), np.rot90(big_tile,3)])

num_monsters = []
for big_tile in big_tile_permutations:
	big_tile_str = '!'.join([''.join(line) for line in big_tile])
	monsters = re.findall(pattern, big_tile_str)
	#print(big_tile_str)
	num_monsters.append(len(monsters))

print(num_monsters)
print(big_tile_str.count('#')-monster.count('#')*max(num_monsters))
