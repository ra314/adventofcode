#Started 16/02/2021 16:31
#Ended 16/02/2021 16:40

myfile = open("input2.txt")
content = myfile.read()
content = sorted(list(content.splitlines()))

import re
guard_sleep_times = {}
for line in content:
	if 'Guard' in line:
		guard_number = int(re.search('#(\d+)', line)[1])
		
	elif 'asleep' in line:
		time_of_sleep = int(re.search(':(\d+)', line)[1])
		
	elif 'wakes' in line:
		time_of_awakening = int(re.search(':(\d+)', line)[1])
		date = re.search('\d\d\d\d-\d\d-\d\d', line)[0]
		minutes_slept = set(range(time_of_sleep, time_of_awakening))
		
		if guard_sleep_times.get(guard_number):
			if guard_sleep_times[guard_number].get(date):
				guard_sleep_times[guard_number][date].update(minutes_slept)
			else:
				guard_sleep_times[guard_number][date] = minutes_slept
		else:
			guard_sleep_times[guard_number] = {}
			guard_sleep_times[guard_number][date] = minutes_slept
			
#Finding the most slept minute for each guard
import collections
most_slept_minute_frequency = 0
most_slept_minute = 0
most_slept_minute_guard_id = 0
for guard in guard_sleep_times:
	minutes_of_sleep = []
	for minutes in guard_sleep_times[guard].values():
		minutes_of_sleep.extend(minutes)
	counter = collections.Counter(minutes_of_sleep)
	
	if counter.most_common(1)[0][1] > most_slept_minute_frequency:
		most_slept_minute, most_slept_minute_frequency = counter.most_common(1)[0]
		most_slept_minute_guard_id = guard
		
print(most_slept_minute_guard_id*most_slept_minute)
