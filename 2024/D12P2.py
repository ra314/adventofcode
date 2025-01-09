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

def perimeter_discount_edges(component: set[tuple[int, int]], graph: nx.Graph) -> int:
  # For each edge in the graph
  # For a horizontal edge, check the pair of nodes below and above.
  total_discount = 0
  for node in component:
    for edge in graph.edges(node):
      # Check if the edge is horizontal
      n1, n2 = edge
      if n1[0] == n2[0]:
        # Check if the node below and above are not in the component
        if (n1[0] + 1, n1[1]) not in component and (n2[0] + 1, n2[1]) not in component:
          # Discount the edge
          total_discount += 1
        if (n1[0] - 1, n1[1]) not in component and (n2[0] - 1, n2[1]) not in component:
          total_discount += 1
      # Check if the edge is vertical
      if n1[1] == n2[1]:
        # Check if the node to the left and right are not in the component
        if (n1[0], n1[1] + 1) not in component and (n2[0], n2[1] + 1) not in component:
          total_discount += 1
        if (n1[0], n1[1] - 1) not in component and (n2[0], n2[1] - 1) not in component:
          total_discount += 1
  return total_discount

def num_sides(component: set[tuple[int, int]], graph: nx.Graph) -> int:
  r = perimeter(component, graph)
  discount = perimeter_discount_edges(component, graph)
  print(r, discount)
  # Divide by 2 because each edge is processed twice.
  return r - (discount//2)

def cost(component: set[tuple[int, int]], graph: nx.Graph) -> int:
  sides = num_sides(component, graph)
  area = len(component)
  print(area, sides)
  print()
  return sides * area

total = 0
for component in nx.connected_components(graph):
  total += cost(component, graph)

print(total)
