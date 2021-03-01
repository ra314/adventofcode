myfile = open("input2.txt")
content = myfile.read()

# Node Class
class node:
	def __init__(self, num):
		self.num = num
		self.prev = None
		self.next = None
		
# Parsing input
cups = [int(num) for num in content.strip()]
cups += list(range(max(cups)+1, 1000000+1))

cups2 = list(range(1000000+1))
#cups2 = list(range(max(cups)+1))
cups2[cups[0]] = node(cups[0])

prev_num = cups[0]
for num in cups[1:]:
	cups2[num] = node(num)
	cups2[num].prev = cups2[prev_num]
	cups2[prev_num].next = cups2[num]
	prev_num = num
	
first_num = cups[0]
last_num = cups[-1]
cups2[first_num].prev = cups2[last_num]
cups2[last_num].next = cups2[first_num]
curr_cup = cups2[first_num]

# Moving cups
def move():
	global cups2
	global curr_cup
	
	picked_cups_nums = [curr_cup.next.num, curr_cup.next.next.num, curr_cup.next.next.next.num]
	destination_cup_num = curr_cup.num
	while True:
		destination_cup_num -= 1
		if destination_cup_num == 0: destination_cup_num = max(cups)
		if destination_cup_num not in picked_cups_nums: break

	#print(picked_cups_nums, destination_cup_num, curr_cup.num)
	
	curr_cup.next = cups2[picked_cups_nums[-1]].next
	cups2[picked_cups_nums[-1]].next.prev = curr_cup
	
	cups2[picked_cups_nums[-1]].next = cups2[destination_cup_num].next
	cups2[destination_cup_num].prev = cups2[picked_cups_nums[-1]]
	
	cups2[destination_cup_num].next = cups2[picked_cups_nums[0]]
	cups2[picked_cups_nums[0]].prev = cups2[destination_cup_num]
	
	curr_cup = curr_cup.next
	
for i in range(10000000):
	move()

#Memory usage
import resource
print(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)

print(cups2[1].next.num * cups2[1].next.next.num)
