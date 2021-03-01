import numpy as np
myfile = open("input2.txt")
content = myfile.read()

timestamp = int(content.splitlines()[0])
bus_ids = np.array(content.splitlines()[1].split(","))
nums_list = [x.isdigit() for x in bus_ids]
bus_ids = bus_ids[nums_list].astype(int)
time_to_bus = bus_ids-timestamp%bus_ids
earliest_bus_index = time_to_bus.argmin()

print(bus_ids[earliest_bus_index]*time_to_bus[earliest_bus_index])
