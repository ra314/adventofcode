#Started 24/02/2021 14:20
#Ended 24/02/2021 16:38

myfile = open("input.txt")
content = myfile.read()
content = content.strip()
num_recipes = int(content)

class Node:
	def __init__(self, num, index):
		self.num = num
		self.index = index
		self.next = None
		self.prev = None
		
start = Node(3,0)
end = Node(7,1)
start.next = end
start.prev = end
end.next = start
end.prev = start

elf1_node = start
elf2_node = end



def add_node(num):
	global start, end
	new_node = Node(num, end.index+1)
	
	new_node.next = start
	new_node.prev = end
	end.next = new_node
	start.prev = new_node
	
	end = new_node
	
def get_next(node, num_nexts):
	while num_nexts != 0:
		num_nexts -=1
		node = node.next
	return node

def create_recipes():
	global elf1_node, elf2_node
	
	new_recipes = str(elf1_node.num + elf2_node.num)
	for char in new_recipes:
		add_node(int(char))

	elf1_node = get_next(elf1_node, elf1_node.num + 1)
	elf2_node = get_next(elf2_node, elf2_node.num + 1)
	
def check_for_match():
	global end
	score = ''
	curr_node = end
	for i in range(len(content)+1):
		score += str(curr_node.num)
		curr_node = curr_node.prev
	score = score[::-1]
	if content in score:
		return end.index - len(content) + score.find(content)
	else:
		return 0

import time
start_time = time.time()
i = 0
while not check_for_match():
	i += 1
	create_recipes()
	
	if time.time() - start_time > 5:
		print(end.index)
		start_time = time.time()

print(check_for_match())
