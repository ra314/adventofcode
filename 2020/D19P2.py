#My previous version of the script used enumeration
#Part 2 of this problem however has infinite loops
#So I'm using a different strategy since enumeration is no longer possible
myfile = open("input.txt")
content = myfile.read()
content = content.splitlines()

#Parsing the text to get the rules and messages
#Rules are stored as a dictionary with the key being the rule number
#and the values being lists containing the rules
#eg: rules['1'] = [['26', '86'], ['114', '32']]
#Messages stored as a list 
import re
rules = {}
messages = []
for line in content:
	if '|' in line:
		nums = re.split("[:|]", line)
		rules[nums[0]] = [nums[1].split(), nums[2].split()]
	elif '"' in line:
		rule_num = re.search("(\d+):", line).group(1)
		char = re.search("\"(.)\"", line).group(1)
		rules[rule_num] = [[char]]
	elif ':' in line:
		nums = re.split("[:]", line)
		rules[nums[0]] = [nums[1].split()]
	else:
		messages.append(line)
del messages[0]

rules['8'] = [['42'],['42','8']]
rules['11'] = [['42','31'],['42','11','31']]

#This function takes a given sequence and looks at the first number in the sequence
#And returns the possible rules that can fill in that spot
#eg: sequence = ['39', '86']
#sequences = [['32', '105', '86'], ['86', '120', '86']]
def get_nums(sequence):
	first_num_in_sequence = sequence[0]
	del sequence[0]
	sequences = [rule+sequence for rule in rules[first_num_in_sequence]]
	return sequences

#This function takes a list of possible sequences
#Takes the first position in each sequence
#If the first position is a digit, it converts it to a char
#If it is a char it checks if it matches the current message_char
#If so it adds this to the checked_possible_sequences list which is returned at the end
#The 'x' is used to signify the end of a sequence
def update(possible_sequences, message_char):
	i = 0
	checked_possible_sequences = []
	while i < len(possible_sequences):
		sequence = possible_sequences[i]
		if sequence[0].isdigit():
			possible_sequences.extend(get_nums(sequence))
		elif sequence[0] == message_char:
			if len(sequence)>1:
				checked_possible_sequences.append(sequence[1:])
			else:
				checked_possible_sequences.append(['x'])
		del possible_sequences[i]
	return checked_possible_sequences

#This function checks the validity of a message
#Possible_sequences starts as rules['0']
#But if it becomes empty, that means the rule is not valid
import copy
def check_message(message):
	possible_sequences = copy.deepcopy(rules['0'])
	for message_index in range(len(message)):
		possible_sequences = update(possible_sequences, message[message_index])
		if len(possible_sequences) == 0:
			return 0
	#This checks if the end of a sequence has been reached
	#Because that's necessary for the message to be valid eg aba != abaab
	if ['x'] in possible_sequences:
		return 1
	else:
		return 0

num_valid_messages = 0
valid_messages = []
for message in messages:
	if message == 'aaaabbaaaabbaaa':
		print("Foudn the wirdo")
	if check_message(message):
		num_valid_messages += 1
		valid_messages.append(message)

print(num_valid_messages)

true_valid_input_3 = ['bbabbbbaabaabba', 'babbbbaabbbbbabbbbbbaabaaabaaa', 'aaabbbbbbaaaabaababaabababbabaaabbababababaaa', 'bbbbbbbaaaabbbbaaabbabaaa', 'bbbababbbbaaaaaaaabbababaaababaabab', 'ababaaaaaabaaab', 'ababaaaaabbbaba', 'baabbaaaabbaaaababbaababb', 'abbbbabbbbaaaababbbbbbaaaababb', 'aaaaabbaabaaaaababaa', 'aaaabbaabbaaaaaaabbbabbbaaabbaabaaa', 'aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba']

#diff = list(set(valid_messages)-set(true_valid_input_3))[0]
