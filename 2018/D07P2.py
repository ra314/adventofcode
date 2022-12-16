#Started 22/02/2021 14:55
#Ended 22/02/2021 15:56

myfile = open("input.txt")
content = myfile.read()

class Node:
	def __init__(self, name):
		self.name = name
		self.prev_nodes = []
		self.worked_on = False
		
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
	return [node for node in nodes.values() if (len(node.prev_nodes)==0 and not node.worked_on)]

class Worker:
	def __init__(self, name):
		self.name = name
		self.node_worked_on = None
		self.time_worked_on_node = 0
		
	def print(self):
		print(f"{self.name}: {self.node_worked_on}")
		
	def work(self):
		if not self.node_worked_on: 
			return False
		self.time_worked_on_node += 1
		return self.time_worked_on_node == (ord(self.node_worked_on.name)-64+60)
		
	def reset(self):
		self.node_worked_on = None
		self.time_worked_on_node = 0

workers = {}
for i in range(5):
	workers[i] = Worker(i)

def assign_node(node):
	for worker in workers.values():
		if not worker.node_worked_on:
			worker.node_worked_on = node
			node.worked_on = True
			return True
	return False

order = []
def remove_node(node_to_remove):
	for node in nodes.values():	
		if node_to_remove.name in node.prev_nodes:
			node.prev_nodes.remove(node_to_remove.name)
			
	order.append(node_to_remove.name)
	del nodes[node_to_remove.name]

time = 0
while nodes: 
	for node in find_bottom_nodes():
		assign_node(node)
	
	print(time, [worker.node_worked_on.name if worker.node_worked_on else '.' for worker in workers.values()], ''.join(order))
	
	for worker in workers.values():
		if worker.work():
			remove_node(worker.node_worked_on)
			worker.reset()
	
	time += 1
	
print(time)
