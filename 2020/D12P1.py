import numpy as np
import math
myfile = open("input.txt")
content = myfile.read()
coordinates = np.array([0,0])
angle = 0
direction_facing = np.array([1,0])



for line in content.splitlines():
	direction = line[0]
	value = int(line[1:])
	
	if direction in "NSEW":
		if direction == "N":
			coordinates[1] += value
		elif direction == "S":
			coordinates[1] -= value
		elif direction == "E":
			coordinates[0] += value
		elif direction == "W":
			coordinates[0] -= value
	
	elif direction == "F":
		direction_facing[1] = math.sin(math.radians(angle))
		direction_facing[0] = math.cos(math.radians(angle))
		coordinates += (direction_facing*value)
		
	elif direction == "L":
		angle += value
		angle %= 360
	
	elif direction == "R":
		angle -= value
		angle %= 360
	
print(sum(abs(coordinates)))
