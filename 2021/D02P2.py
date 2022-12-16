import numpy as np
myfile = open("input.txt")
content = myfile.read()

hor = 0
vert = 0
aim = 0

for line in content.splitlines():
    direction = line.split()[0]
    distance = int(line.split()[1])
    if direction == "forward":
        hor += distance
        vert += (aim * distance)
    elif direction == "down":
        aim += distance
    elif direction == "up":
        aim -= distance
    #print(hor, vert, aim)

print(hor*vert)
