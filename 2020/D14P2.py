myfile = open("input.txt")
content = myfile.read()

def bitmask(mask, addr):
	b2addr = '{0:036b}'.format(addr)
	masked = ''
	for (mask_char, addr_char) in zip(mask, b2addr):
		if mask_char in '1X':
			masked += mask_char
		else:
			masked += addr_char
	return masked
	
def genaddresses(addr):
	addr_list = [addr]
	i = 0
	
	while True:
		if i == len(addr_list): break
		addr = addr_list[i]
		
		if 'X' not in addr:
			i+=1
			continue

		index = addr.find('X')
		addr_list.append(addr[:index] + '0' + addr[index+1:])
		addr_list.append(addr[:index] + '1' + addr[index+1:])

		addr_list.pop(i)
		
	return addr_list
	
	
memory = {}
for line in content.splitlines():
	if line[1] == 'a':
		mask = line.split()[2]
	else:
		addr = int(line.split(']')[0][4:])
		value = int(line.split()[-1])
		addr_list = genaddresses(bitmask(mask, addr))
		for addr in addr_list:
			memory[addr] = value

sum = 0
for key, value in memory.items():
	sum += value

print(sum)
