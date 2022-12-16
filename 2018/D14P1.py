#Started 24/02/2021 13:55
#Ended 24/02/2021 14:19

myfile = open("input.txt")
content = myfile.read()
num_recipes = int(content)

recipes = [3,7]
elf1_recipe_index = 0
elf2_recipe_index = 1

def create_recipes():
	global elf1_recipe_index, elf2_recipe_index, recipes
	new_recipes = [int(char) for char in str(recipes[elf1_recipe_index] + recipes[elf2_recipe_index])]
	recipes.extend(new_recipes)
	elf1_recipe_index = (elf1_recipe_index + recipes[elf1_recipe_index] + 1)%len(recipes)
	elf2_recipe_index = (elf2_recipe_index + recipes[elf2_recipe_index] + 1)%len(recipes)

while len(recipes) < num_recipes+10:
	create_recipes()
	#print(recipes)

print("".join([str(num) for num in recipes[num_recipes:num_recipes+10]]))