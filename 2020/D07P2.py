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
			if i>4 and string[i-2] != "no":
				colors.append([int(string[i-3]), string[i-2] + ' ' + string[i-1]])
			else:
				colors.append(string[i-2] + ' ' + string[i-1])
	return colors

for rule in content:
	colors = get_colors(rule)
	colors_dict[colors[0]] = colors[1:]
	
def count_bags(curr_color):
	if colors_dict.get(curr_color) == ["no other"]:
		return 0
	
	sum = 0
	for color in colors_dict.get(curr_color):
		sum += ((count_bags(color[1]) * color[0]) + color[0])
		
	return sum
	
print(count_bags(target))
