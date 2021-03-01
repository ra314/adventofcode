myfile = open("input3.txt")
content = myfile.read()
content = content.splitlines()

#Parsing the text to get the rules and messages
import re
rules = {}
messages = []
for line in content:
	if '|' in line:
		nums = re.split("[:|]", line)
		rules[nums[0]] = [[nums[1].split(), nums[2].split()], False]
	elif '"' in line:
		rule_num = re.search("(\d+):", line).group(1)
		char = re.search("\"(.)\"", line).group(1)
		rules[rule_num] = [[[char]], True]
	elif ':' in line:
		nums = re.split("[:]", line)
		rules[nums[0]] = [[nums[1].split()], False]
	else:
		messages.append(line)
del messages[0]

longest_message_len = max([len(message) for message in messages])

def solve(key):
	rule, enumerated = rules[key]
	if enumerated:
		return rule
	i=0
	while i < len(rule):
		variation = rule[i]
		j=0
		while j < len(variation):
			variation = rule[i]
			char = variation[j]
			if char.isdigit():
				results = solve(char)
				to_append_to_rule = []
				for result in results:
					to_append_to_rule.append(variation[:j]+result+variation[j+1:])
				rule = rule[:i] + to_append_to_rule + rule[i+1:]
				rules[key] = [rule, False]
			else:
				j+=1
		i+=1
	rules[key] = [rules[key][0], True]
	return rule
	
solve('0')

possible_valid_messages = []
for message in rules['0'][0]:
	possible_valid_messages.append("".join(message))
num_messages_matching = 0
valid_messages = []
for message in messages:
	if message in possible_valid_messages:
		valid_messages.append(message)
		num_messages_matching += 1

print(num_messages_matching)
print(valid_messages)
