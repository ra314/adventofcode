import numpy as np
myfile = open("input.txt")
content = myfile.read()

array = []
for line in content.splitlines():
    array.append((list(map(int, line))))

array = np.array(array)

def generate_adjacents(coordinate):
    adjacents = []
    for i in [-1,0,1]:
        for j in [-1,0,1]:
            if i == 0 and j == 0:
                continue
            adjacents.append(coordinate + np.array([i,j]))
    # Remove coordiantes that are out of grid
    adjacents = list(filter(lambda x: x[0]>=0 and x[0]<=9 and x[1]>=0 and x[1]<=9, adjacents)) 
    return adjacents

def flash(flash_loc, array, has_flashed):
    for adjacent in generate_adjacents(flash_loc):
        array[tuple(adjacent)] += 1
    has_flashed[tuple(flash_loc)] = True

def cycle(array):
    # Step 1
    array += 1
    # Step 2
    has_flashed = np.full((10, 10), False)
    while np.bitwise_and((array>9), np.bitwise_not(has_flashed)).sum():
        flashes = array > 9
        flash_locs = list(map(list, np.where(np.bitwise_and((array>9), np.bitwise_not(has_flashed)))))
        for flash_loc in list(zip(flash_locs[0], flash_locs[1])):
            flash(flash_loc, array, has_flashed)
    # Step 3
    array[array>9] = 0
    return has_flashed.sum() == 100

i = 0
while True:
    i += 1
    if cycle(array):
        print(i)
        break
