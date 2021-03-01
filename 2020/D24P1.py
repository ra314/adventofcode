'''Note that the order of the directions doesn't matter
so NESE = SENE
So this means that anytime NE+SE comes up you can simplify that to E
There a couple other simplificiationca that can be made
E+W = 0
NE+SW = 0
NW+SE = 0
etc
Use this to create unique addresses for each hex and then count the flips'''

myfile = open("input2.txt")
content = myfile.read()

# Parsing input
addresses = []
for line in content.splitlines():
	i=0
	address = []
	while i < len(line):
		if line[i] in 'ew':
			address.append(line[i])
			i+=1
		else:
			address.append(line[i:i+2])
			i+=2
	addresses.append(address)
	
# Simplifying addresses
# These directions cancel eachother out
# Moving e + w = 0
cancelling_pairs = [['e','w'],['ne','sw'],['nw','se']]
# The first two direction simplify into the third
# So moving ne + se = e
simplifying_pairs = [['e','nw','ne'],['ne','w','nw'],['nw','sw','w'],['w','se','sw'],['sw','e','se'],['ne','se','e']]

for address in addresses:
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
		
addresses = [''.join(sorted(address)) for address in addresses]

# Counting black tiles
import collections
num_black_tiles = sum([value%2 for value in collections.Counter(addresses).values()])
print(num_black_tiles)
