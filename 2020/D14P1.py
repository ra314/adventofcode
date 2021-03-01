myfile = open("input.txt")
content = myfile.read()

def bitmask(mask, val):
	b2val = '{0:036b}'.format(val)
	masked = ''
	for (mask_char, val_char) in zip(mask, b2val):
		if mask_char in '01':
			masked += mask_char
		else:
			masked += val_char
	return int(masked, 2)

memory = {}

for line in content.splitlines():
	if line[1] == 'a':
		mask = line.split()[2]
	else:
		position = line.split(']')[0][4:]
		value = int(line.split()[-1])
		memory[position] = bitmask(mask, value)

sum = 0
for key, value in memory.items():
	sum += value

print(sum)
	
