#Started 22/02/2021 19:32
#Ended 22/02/2021 19:33

myfile = open("input.txt")
content = myfile.read()

class Node:
	def __init__(self, name):
		self.name = name
		self.prev = None
		self.next = None

import re
num_players = int(re.search('^\d+', content)[0])
last_marble = int(re.search('is worth (\d+)', content)[1])*100
player_scores = [0]*(num_players+1)

first_node = Node(0)
first_node.next = first_node
first_node.prev = first_node

#node 1 is the node being inserted
#It is to be place after node 2
def insert_node_after(node1, node2):
	node1.next = node2.next
	node1.prev = node2
	node2.next.prev = node1
	node2.next = node1
	
def remove_node(node):
	node.prev.next = node.next
	node.next.prev = node.prev

curr_player = 1
curr_node = first_node
for i in range(1,last_marble+1):
	curr_player = (curr_player+1)%num_players
	if i%23 == 0:
		player_scores[curr_player] += i
		seven_nodes_ago = curr_node.prev.prev.prev.prev.prev.prev.prev
		player_scores[curr_player] += seven_nodes_ago.name
		curr_node = seven_nodes_ago.next
		remove_node(seven_nodes_ago)
	else:
		insert_node_after(Node(i), curr_node.next)
		curr_node = curr_node.next.next

print(max(player_scores))
