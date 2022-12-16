import numpy as np
myfile = open("input.txt")
content = myfile.read()

array = []
for line in content.splitlines():
    array.append((list(map(int, line))))

array = np.array(array)

from dijkstar import Graph, find_path
graph = Graph()

def generate_adjacents(coordinate):
    adjacents = []
    for i in [-1,0,1]:
        for j in [-1,0,1]:
            if abs(i) + abs(j) != 1:
                continue
            adjacents.append(coordinate + np.array([i,j]))
    # Remove coordiantes that are out of grid
    adjacents = list(filter(lambda x: x[0]>=0 and x[0]<array.shape[0] and x[1]>=0 and x[1]<array.shape[1], adjacents)) 
    return adjacents

def create_node_name(coordinate):
    return f"x:{coordinate[0]},y:{coordinate[1]}"

for i in range(array.shape[0]):
    for j in range(array.shape[1]):
        for adjacent in generate_adjacents([i,j]):
            node1 = create_node_name([i,j])
            node2 = create_node_name(adjacent)
            weight = array[adjacent[0],adjacent[1]]
            graph.add_edge(node1, node2, weight)

path = find_path(graph, create_node_name((0,0)), create_node_name(np.array(array.shape)-1))
print(path.total_cost)
