myfile = open("input.txt")
content = myfile.read()

import numpy as np

#Converts the tile from a string into a binary numpy array
def convert_tile(tile):
	return np.array([[1 if char == '#' else 0 for char in line] for line in tile.splitlines()])
	
import re
#Reads the input file and finds strings that refer to the tile number and the tile itself
def parse_tiles(content):
	tile_nums = re.findall('\d+', content)
	tiles = [convert_tile(tile[0]) for tile in re.findall('(([.#]+\n)+)', content)]
	return zip(tile_nums, tiles)

class Tile:
	def __init__(self, tile_num, tile):
		self.tile_num = tile_num
		self.tile = tile
		self.edges = [list(edge) for edge in [tile[0,:], tile[:,-1], tile[:,0], tile[-1,:]]]
		self.neighbours = []
		
#Converts all of the found tiles into Tile objects
tiles = {}
for tile_num, tile in parse_tiles(content):
	tiles[tile_num] = Tile(tile_num, tile)
	
#This function compares the edges between two tiles for a match
def compare_edges(tile1, tile2):
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
			compare_edges(tile1, tile2)

def print_all_neighbours():
	for tile in tiles.values():
		print(tile.tile_num, [neighbour.tile_num for neighbour in tile.neighbours])
		
corners = [int(tile.tile_num) for tile in tiles.values() if len(tile.neighbours)==2]
print(corners)
print(np.product(corners))

#Thoughts
#Just had a revelation that you don't need to find the location for each of the tiles.
#All you have to do is find the IDs of the corner tiles and find the product
#And to do that all you need to do is find all tiles that only have 2 neighbours.
