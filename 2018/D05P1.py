#Started 16/02/2021 17:35
#Ended 16/02/2021 18:22

myfile = open("input.txt")
content = myfile.read()

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

print(len(process_polymer(list(content)))-1)
