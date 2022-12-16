import numpy as np
myfile = open("input.txt")
content = myfile.read()

hor = 0
vert = 0
for line in content.splitlines():
    direction = line.split()[0]
    distance = int(line.split()[1])
    if direction == "forward":
        hor += distance
    elif direction == "down":
        vert += distance
    elif direction == "up":
        vert -= distance

print(hor*vert)
