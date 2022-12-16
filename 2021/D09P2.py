import numpy as np
myfile = open("input2.txt")
content = myfile.read()

matrix = np.array(list(map(list, content.split()))).astype('int')
bool_matrix = np.zeros(matrix.shape)

# Check right neighobour
bool_matrix[:,:-1] += matrix[:,:-1]<matrix[:,1:]
# Check left
bool_matrix[:,1:] += matrix[:,1:]<matrix[:,:-1]
# Check up
bool_matrix[1:,:] += matrix[1:,:]<matrix[:-1,:]
# Check down
bool_matrix[:-1,:] += matrix[:-1,:]<matrix[1:,:]

# Add 1's along the edges, for cells that can't be smaller than their neighbours, since the neighbour doesn't exist
bool_matrix[0] += 1
bool_matrix[-1] += 1
bool_matrix[:,0] += 1
bool_matrix[:,-1] += 1

print(sum(matrix[bool_matrix==4]+1))

from skimage.segmentation import flood, flood_fill
def get_basin_size(low_point, matrix):
    return (flood_fill(matrix, low_point, -100, connectivity=1)==-100).sum()

coords = list(map(list, np.where(bool_matrix==4)))
basin_sizes = []
for coord in zip(coords[0], coords[1]):
    basin_sizes.append(get_basin_size(coord, matrix))

a = sorted(basin_sizes)[-3:]
print(a[0]*a[1]*a[2])
