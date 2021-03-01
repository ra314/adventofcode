import numpy as np
import math
myfile = open("input.txt")
content = myfile.read()

timestamp = int(content.splitlines()[0])
bus_ids = np.array(content.splitlines()[1].split(","))

nums_list = [x.isdigit() for x in bus_ids]
bus_offsets = np.array(range(len(bus_ids)))[nums_list]
bus_ids = bus_ids[nums_list].astype(int)

def gen_bits(bus_id, offset, index, length):
	curr = np.ones(bus_id)
	curr[0] = 0
	start = np.array([1]*(bus_id - (index%bus_id) - offset))
	end = np.tile(curr, math.ceil(length/bus_id))
	return np.concatenate([start, end])[:length]

def find_timestamp_4(timestamp):
	increment = 1
	max_num_matching = 0
	match_locations = [False]*len(bus_ids)
	while True:
		matches = (bus_offsets+timestamp)%bus_ids
		num_matching = sum(matches==0)
		
		if num_matching == len(bus_ids):
			return timestamp
		
		if num_matching > max_num_matching:
			for i in range(len(matches)):
				if not match_locations[i] and matches[i]==0:
					match_locations[i] = True
					increment *= bus_ids[i]
					break
			max_num_matching = num_matching
			
		timestamp += increment

def find_timestamp_3(timestamp, increment):
	while True:
		sum = np.zeros(increment)
		for i in range(len(bus_ids)):
			sum += gen_bits(bus_ids[i], bus_offsets[i], timestamp, increment)
		if sum.min() == 0:
			return timestamp + sum.argmin(), sum.min()
		timestamp += increment
		print(timestamp)

def find_timestamp_2(timestamp, increment):
	while True:
		timestamps_to_test = np.array(range(increment)) + timestamp
		sum = np.zeros(increment)
		for i in range(len(bus_ids)):
			sum += (timestamps_to_test + bus_offsets[i])%bus_ids[i]

		if sum.min() == 0:
			return timestamps_to_test[sum.argmin()]
		
		timestamp += increment

def find_timestamp_1(timestamp):
	big_id = bus_ids.max()
	big_offset = bus_offsets[bus_ids.argmax()]
	timestamp += big_id-((big_offset+timestamp)%big_id)

	add_array = np.array(range(10)).reshape(1,10)

	while True:
		if not np.all(((bus_offsets+timestamp)%bus_ids)==0):
			timestamp += big_id
			#print(timestamp)
			continue
				
		return timestamp
		break
		
'''		
I was having trouble with my bruteforce methods.
In even my best bruteforce method the biggest increment in timestamp was the biggest bus id.
Even vectorizing the operations in numpy wasn't enough.
Then I realized one morning that I could increment by the LCM of some busids.
So for example if I come upon a timestamp that agrees with the requirements for bus_id 7 and 13, then I could start incrementing by (7*13) since that's the LCM and every increment would satisfy 7 and 13 which is necessary for the final solution anyway. and we wouldn't be skipping any timestampts that would also satisfyin both 7 and 13.
'''
