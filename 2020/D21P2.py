myfile = open("input.txt")
content = myfile.read()

###This is a dictionary where the key is each allergen
###The values will be a list
###The first value of the tuple is the possible ingredient that the allergen could be in each line
###The second value of the tuple is a boolean to show whether the ingredient that the allergen corresponds to has been determined
allergens_dict = {}

###Parsing the content to getthe allergens and ingredients in each line
for line in content.splitlines():
	ingredients = line[:line.index('(')].split()
	allergens = line[line.index('contains')+len('contains'):-1].replace(" ","").split(',')
	for allergen in allergens:
		if allergens_dict.get(allergen):
			allergens_dict[allergen][0].append(ingredients)
		else:
			allergens_dict[allergen] = [[ingredients], False]
			
###Now we process the dictionary
###The values are lists of ingredients that the allergen could possibly be
###We remove ingredients that are not present in all of the lists for the same allergen
for allergen in allergens_dict:
	allergens_dict[allergen][0] = list(set(allergens_dict[allergen][0][0]).intersection(*allergens_dict[allergen][0]))
	
###Now we go through the dictionary and find allergens that have a determined ingredient
###And remove these ingredients as possibilities from other allergens
def remove_ingredient(ingredient, input_allergen):
	for allergen in allergens_dict:
		if allergen == input_allergen: continue
		if allergens_dict[allergen][1]: continue
		if ingredient in allergens_dict[allergen][0]:
			allergens_dict[allergen][0].remove(ingredient)
			
def are_all_allergens_isolated():
	for allergen in allergens_dict:
		if not allergens_dict[allergen][1]:
			return False
	return True

while not are_all_allergens_isolated():
	for allergen in allergens_dict:
		if len(allergens_dict[allergen][0]) == 1:
			remove_ingredient(allergens_dict[allergen][0][0], allergen)
			allergens_dict[allergen][1] = True
		
allergenic_ingredients = [item[0][0] for item in allergens_dict.values()]

###Counting the occurence of non_allergenic_ingredients
num_non_allergenic_ingredients = 0
all_ingredients = []
for line in content.splitlines():
	all_ingredients.extend(line[:line.index('(')].split())
	
for ingredient in all_ingredients:
	if ingredient not in allergenic_ingredients:
		num_non_allergenic_ingredients += 1
		
print(num_non_allergenic_ingredients)

###Printing all the allergenic ingredients alphabetically
allergens = list(allergens_dict.keys())
ingredients = [item[0][0] for item in allergens_dict.values()]
allergens, ingredients = zip(*sorted(zip(allergens, ingredients)))
print(','.join(ingredients))
