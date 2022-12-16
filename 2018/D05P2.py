#Started 16/02/2021 18:22
#Ended 16/02/2021 18:31

myfile = open("input2.txt")
content = myfile.read()
content = list(content)

def process_polymer(polymer):
	i = 0
	while i < len(polymer)-2:
		if polymer[i].isupper():
			if polymer[i+1].islower() and polymer[i+1].upper() == polymer[i]:
				del polymer[i:i+2]
				i-=1
				continue
		else:
			if polymer[i+1].isupper() and polymer[i+1].lower() == polymer[i]:
				del polymer[i:i+2]
				i-=1
				continue
		i+=1
	return polymer

min_len = len(content)
min_len_char = ''

for char in set([char.lower() for char in set(content)]):
	new_content = content.copy()
	new_content = list(filter(lambda a: a not in (char.upper(), char.lower()), new_content))
	new_len = len(process_polymer(new_content))
	if new_len < min_len:
		min_len = new_len
		min_len_char = char
		
print(min_len-1)
