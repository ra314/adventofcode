import numpy as np
myfile = open("input.txt")
content = myfile.read()

nums = list(map(int, content.split(',')))

import functools
@cache
def num_children(curr_num, num_days):
    if curr_num < num_days:
        return num_children(6, num_days - curr_num-1) + num_children(8, num_days - curr_num-1)
    else:
        return 1


total = 0
for num in nums:
    total += num_children(num, 256)

