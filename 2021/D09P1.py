import numpy as np
myfile = open("input.txt")
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
