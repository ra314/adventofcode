#Started 22/02/2021 18:10
#Ended 22/02/2021 18:32

myfile = open("input.txt")
content = myfile.read()
content = [int(num) for num in content.split()]

class Node:
	def __init__(self, name):
		self.name = name
		self.metadata = []
		self.children = []
		
	def print(self):
		print(f"{self.name}: {self.children}")

#The function returns the number of nums to skip to get to the metadata and also generates node
node_counter = 1

def build_tree(data):
	global node_counter
	node = Node(chr(node_counter+64))
	num_children = data[0]
	num_metadata = data[1]
	num_to_skip = 0
	
	children_processed = 0
	while children_processed != num_children:
		child, skip_increment = build_tree(data[2+num_to_skip:])
		node.children.append(child)
		num_to_skip += skip_increment
		children_processed += 1
		
	#print(num_children, num_metadata, data[2+num_to_skip:2+num_to_skip+num_metadata])
	node.metadata = data[2+num_to_skip:2+num_to_skip+num_metadata]
	node_counter += 1
	return node, num_metadata + 2 + num_to_skip
	
root_node = build_tree(content)[0]

def calculate_value(node):
	value = 0
	if len(node.children) == 0:
		return sum(node.metadata)
		
	for num in node.metadata:
		if num <= len(node.children):
			value += calculate_value(node.children[num-1])
	return value
	
print(calculate_value(root_node))
