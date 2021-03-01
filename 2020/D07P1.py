myfile = open("input.txt")
content = myfile.read()
content = content.splitlines()

colors_dict = {}
target = "shiny gold"

def get_colors(string):
	colors = []
	string = string.split()
	for i in range(len(string)):
		if "bag" in string[i]:
			colors.append(string[i-2] + ' ' + string[i-1])
	return colors

for rule in content:
	colors = get_colors(rule)
	colors_dict[colors[0]] = colors[1:]
	
def can_hold_gold(curr_color):
	if curr_color == "no other":
		return False
	if colors_dict.get(curr_color) == []:
		return False
	if "shiny gold" in colors_dict.get(curr_color):
		return True
	if len(colors_used) == len(colors_dict):
		return False
	for color in colors_dict.get(curr_color):
		if can_hold_gold(color): return True
	return False
	
num_containing = 0
for color in colors_dict.keys():
	colors_used = []
	if can_hold_gold(color):
		num_containing += 1
		
print(num_containing)
