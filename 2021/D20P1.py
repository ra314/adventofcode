import numpy as np
myfile = open("input.txt")
content = myfile.read()

image_enhancement = content.splitlines()[:content.splitlines().index('')]
image_enhancement = "".join(image_enhancement)
image_enhancement = np.array([0 if char == '.' else 1 for char in image_enhancement])

image = content.splitlines()[content.splitlines().index('')+1:]
image = np.array(list(map(lambda x: [0 if char == '.' else 1 for char in x], image)))

def generate_adjacents(coordinate, grid_shape):
    adjacents = []
    for i in [-1,0,1]:
        for j in [-1,0,1]:
            adjacents.append(coordinate + np.array([i,j]))
    # Remove coordiantes that are out of grid
    adjacents = list(filter(lambda x: x[0]>=0 and x[0]<grid_shape[0] and x[1]>=0 and x[1]<grid_shape[1], adjacents)) 
    return adjacents

def convert_to_binary(coordinates, image):
    adjacents = generate_adjacents(coordinates, image.shape)
    binary_string = ""
    for adjacent in adjacents:
        binary_string += str(image[adjacent[0],adjacent[1]])
    return int(binary_string, 2)

def enhance_image(image, i):
    if image_enhancement[0] == 1:
        if i%2 == 0:
            new_image = np.zeros(np.array(image.shape)+4).astype('int')
        else:
            new_image = np.ones(np.array(image.shape)+4).astype('int')
    else:
        new_image = np.zeros(np.array(image.shape)+4).astype('int')
    new_image[2:image.shape[0]+2,2:image.shape[1]+2] += image
    image = np.copy(new_image)
    for i in range(1,len(image)-1):
        for j in range(1,len(image)-1):
            new_image[i,j] = image_enhancement[convert_to_binary((i,j), image)]
    return new_image

def convert_to_string(image):
    string = ""
    for line in image:
        string += "".join(["#" if x else "." for x in line]) + "\n"
    return string

for i in range(2):
    image = enhance_image(image, i)

print(convert_to_string(image))
print(image.sum())
