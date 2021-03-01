import numpy as np
import math
myfile = open("input.txt")
content = myfile.read()
waypoint_coordinates = np.array([10,1])
ship_coordinates = np.array([0,0])

def R90(coordinates):
	return np.array([coordinates[1], -coordinates[0]])
	
def get_new_waypoint(waypoint_coordinates, angle_change, direction):
	if direction == "L":
		angle_change = 360 - angle_change
	for i in range(int(angle_change/90)):
		waypoint_coordinates = R90(waypoint_coordinates)
	return waypoint_coordinates

for line in content.splitlines():
	direction = line[0]
	value = int(line[1:])
	
	if direction in "NSEW":
		if direction == "N":
			waypoint_coordinates[1] += value
		elif direction == "S":
			waypoint_coordinates[1] -= value
		elif direction == "E":
			waypoint_coordinates[0] += value
		elif direction == "W":
			waypoint_coordinates[0] -= value
	
	elif direction == "F":
		ship_coordinates = ship_coordinates+(waypoint_coordinates*value)
		
	elif direction in "RL":
		waypoint_coordinates = get_new_waypoint(waypoint_coordinates, value, direction)
		
	print(line)
	print(waypoint_coordinates)
	print(ship_coordinates)
	
print(sum(abs(ship_coordinates)))
