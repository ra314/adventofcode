#Started 16/02/2021 15:27
#Ended 16/02/2021 16:30

myfile = open("input.txt")
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
			
#Finding the guard that slept the most
longest_sleep_time = 0
longest_sleep_guard_id = 0
for guard in guard_sleep_times:
	curr_sleep_time = sum([len(minutes) for minutes in guard_sleep_times[guard].values()])
	if curr_sleep_time > longest_sleep_time:
		longest_sleep_time = curr_sleep_time
		longest_sleep_guard_id = guard

#Finding the most slept minute
minutes_of_sleep = []
for minutes in guard_sleep_times[longest_sleep_guard_id].values():
	minutes_of_sleep.extend(minutes)
import collections
counter = collections.Counter(minutes_of_sleep)
most_slept_minute = counter.most_common(1)[0][0]

print(most_slept_minute*longest_sleep_guard_id)
