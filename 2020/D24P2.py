myfile = open("input.txt")
content = myfile.read()

# Parsing input
def convert_address_to_list(address_str):
	i=0
	address = []
	while i < len(address_str):
		if address_str[i] in 'ew':
			address.append(address_str[i])
			i+=1
		else:
			address.append(address_str[i:i+2])
			i+=2
	return address
			
addresses = [convert_address_to_list(line) for line in content.splitlines()]

# Simplifying addresses
# These directions cancel eachother out
# Moving e + w = 0
cancelling_pairs = [['e','w'],['ne','sw'],['nw','se']]
# The first two direction simplify into the third
# So moving ne + se = e
simplifying_pairs = [['e','nw','ne'],['ne','w','nw'],['nw','sw','w'],['w','se','sw'],['sw','e','se'],['ne','se','e']]

def simplify(address):
	changed = True
	while changed:
		changed = False
		for pair in simplifying_pairs:
			if pair[0] in address and pair[1] in address:
				address.remove(pair[0])
				address.remove(pair[1])
				address.append(pair[2])
				changed = True
			
	for pair in cancelling_pairs:
		while pair[0] in address and pair[1] in address:
			address.remove(pair[0])
			address.remove(pair[1])
	
	return ''.join(sorted(address))

addresses = [simplify(address) for address in addresses]

# Creating a dictionary of tiles
# Keys are addresses for the tiles
# Values are booleans: True = black, False = white, 
addresses_dict = {}
import collections
for address, times_flipped in collections.Counter(addresses).items():
	addresses_dict[address] = (times_flipped%2)!=0

# Flipping tiles every day
def get_num_adjacent_black(address):
	num_black = 0
	for direction in ['e','ne','nw','w','sw','se']:
		new_address = simplify(convert_address_to_list(address+direction))
		if addresses_dict.get(new_address):
			num_black += addresses_dict[new_address]
	return num_black
	
def process_tile(address):
	num_black = get_num_adjacent_black(address)
	curr_color = addresses_dict[address]
	if curr_color:
		#optimize by deleting cell if it has no adjacent blacks
		if num_black==0 or num_black>2:
			return False
	else:
		if num_black == 2:
			return True
	return curr_color
	
def add_adjacent_to_dict():
	for address in list(addresses_dict.keys()):
		for direction in ['e','ne','nw','w','sw','se']:
			new_address = simplify(convert_address_to_list(address+direction))
			if not addresses_dict.get(new_address):
				addresses_dict[new_address] = False
		
def simulate_flipping(days):
	global addresses_dict
	for i in range(days):
		# Spawning tiles adjacent to all currently considered tiles
		add_adjacent_to_dict()
		new_addresses_dict = addresses_dict.copy()
		
		# Calculating each tile
		for address in new_addresses_dict:
			new_addresses_dict[address] = process_tile(address)
			
		# Pruning tiles that have no black neighrours
		for address in list(new_addresses_dict.keys()):
			if not get_num_adjacent_black(address):
				del new_addresses_dict[address]
		addresses_dict = new_addresses_dict
		print(f"Day {i+1}: {sum(addresses_dict.values())}")
		
simulate_flipping(100)
