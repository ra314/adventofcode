#Started 23/02/2021 16:50
#Ended 23/02/2021 18:49

myfile = open("input.txt")
content = myfile.read()

#Parsing input
import re
initial_state = re.search('state: ([.#]+)', content)
notes = re.findall('([.#]+) => ([.#])', content)

def convert(state):
	if '#' in state or '.' in state:
		return [1 if char == '#' else 0 for char in list(state)]
	else:
		return ''.join(['#' if num == 1 else '.' for num in state])

rules = {}
for note in notes:
	rules[note[0]] = convert(note[1])[0]
	
state = initial_state[1]
padding = '.....'
zero_position = 0

def reproduce():
	global state
	global zero_position
	state = padding + state + padding
	new_state = convert(state)
	zero_position += 5
	for i in range(len(state)-3):
		if state[i-2:i+3] not in rules:
			new_state[i] = 0
		else:
			new_state[i] = rules[state[i-2:i+3]]
	
	state = convert(new_state)
	zero_position -= state.index('#')
	state = re.search('#.*#', state)[0]

for i in range(20):
	reproduce()
	
#Finding sum
import numpy as np
state = np.array(convert(state))
indices = np.arange(-zero_position, len(state)-zero_position)
print(sum(state*indices))
