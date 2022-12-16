#Started 22/02/2021 14:26
#Ended 22/02/2021 14:54

myfile = open("input2.txt")
content = myfile.read()

class Node:
	def __init__(self, name):
		self.name = name
		self.prev_nodes = []
		
	def print(self):
		print(f"{self.name}: {self.prev_nodes}")
		
#Parsing Input and creating nodes
nodes = {}
for line in content.splitlines():
	if line[36] not in nodes.keys():
		nodes[line[36]] = Node(line[36])
		
	nodes[line[36]].prev_nodes.append(line[5])
	
	if line[5] not in nodes.keys():
		nodes[line[5]] = Node(line[5])
	
#Topological Sorting by finding nodes with no prev nodes
def find_bottom_nodes():
	return [node for node in nodes.values() if len(node.prev_nodes)==0]
	
def remove_node(node_to_remove):
	for node in nodes.values():	
		if node_to_remove.name in node.prev_nodes:
			node.prev_nodes.remove(node_to_remove.name)
			
	del nodes[node_to_remove.name]
	
order = []
while nodes:
	bottom_node = min(find_bottom_nodes(), key=lambda x: x.name)
	order.append(bottom_node.name)
	remove_node(bottom_node)
	
print(''.join(order))
