myfile = open("input2.txt")
content = myfile.read()

# Parsing input
cups = [int(num) for num in content.strip()]

# Moving cups
def move():
	global cups
	curr_cup = cups[0]
	picked_cups = cups[1:4]
	del cups[1:4]
	destination_cup = curr_cup - 1
	
	while destination_cup not in cups:
		destination_cup = (destination_cup-1) % (max(cups)+1)
	
	cups[cups.index(destination_cup)+1:cups.index(destination_cup)+1] = picked_cups
	cups.append(cups[0])
	del cups[0]
	
for i in range(100):
	move()
	
cups = cups[cups.index(1):] + cups[:cups.index(1)]
print(''.join([str(num) for num in cups[1:]]))
