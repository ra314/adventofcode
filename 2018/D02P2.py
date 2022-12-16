#Started 16/02/2021 14:27
#Ended 16/02/2021 14:40

myfile = open("input.txt")
content = myfile.read()

#Eg. Takes a string "hello"
#And returns {"h0", "e1", "l2", "l3", "o4"}
def generate_set_with_indexes(string):
	output = set()
	for i in range(len(string)):
		output.add(string[i]+str(i))
	return output

import itertools
for pair in itertools.combinations(content.splitlines(), 2):
	set0 = generate_set_with_indexes(pair[0])
	set1 = generate_set_with_indexes(pair[1])
	if len(set0.difference(set1)) == 1:
		break
		
ID_without_different_char = list(pair[0])
ID_without_different_char.remove(list(set0.difference(set1))[0][0])
ID_without_different_char = ''.join(ID_without_different_char)
print(ID_without_different_char)
