import reader
content = reader.read()

# Create a graph
# For each component of the graph, the perimeter length is the 
# (number of nodes in the component * 4) - (number of edges in the component *2)
import networkx as nx
graph = nx.Graph()
grid = list(map(list, content.splitlines()))
for i in range(len(grid)):
  for j in range(len(grid[i])):
    key = (i,j)
    graph.add_node(key)
    value = grid[i][j]
    # Check if adjacent cells have the same value
    if i > 0 and grid[i-1][j] == value:
      graph.add_edge(key, (i-1,j))
    if i < len(grid) - 1 and grid[i+1][j] == value:
      graph.add_edge(key, (i+1,j))
    if j > 0 and grid[i][j-1] == value:
      graph.add_edge(key, (i,j-1))
    if j < len(grid[i]) - 1 and grid[i][j+1] == value:
      graph.add_edge(key, (i,j+1))

def perimeter(component: set[tuple[int, int]], graph: nx.Graph) -> int:
  num_edges = 0
  for node in component:
    num_edges += len(graph.edges(node))
  return (len(component) * 4) - (num_edges)

def cost(component: set[tuple[int, int]], graph: nx.Graph) -> int:
  return perimeter(component, graph) * len(component)

total = 0
for component in nx.connected_components(graph):
  total += cost(component, graph)
  
print(total)
