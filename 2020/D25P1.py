myfile = open("input.txt")
content = myfile.read()

card_public_key = int(content.splitlines()[0])
door_public_key = int(content.splitlines()[1])

def transform(subject_number, value):
	return (value * subject_number) % 20201227
	
def crack_loop_size(subject_number, public_key):
	value = 1
	i = 0
	while value != public_key:
		value = transform(subject_number, value)
		i += 1
	return i
	
door_loop_size = crack_loop_size(7, door_public_key)
card_loop_size = crack_loop_size(7, card_public_key)

value = 1
for i in range(door_loop_size):	
	value = transform(card_public_key, value)
encryption_key = value

print(encryption_key)
