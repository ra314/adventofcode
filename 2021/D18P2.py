import numpy as np
myfile = open("input.txt")
content = myfile.read()

def parse_line(line):
    nums = []
    depths = []
    depth = -1
    for char in line:
        if char == "[":
            depth += 1
        elif char == "]":
            depth -= 1
        elif char.isdigit():
            nums.append(int(char))
            depths.append(depth)
    return nums, depths

def parse_content(content):
    nums = []
    depths = []
    for line in content.splitlines():
        if not nums:
            nums, depths = parse_line(line)
            depths = np.array(depths)
        else:
            temp_nums, temp_depths = parse_line(line)
            nums += temp_nums
            depths += 1
            temp_depths = np.array(temp_depths)
            temp_depths += 1
            depths = np.concatenate((depths, temp_depths))
            nums, depths = reduce_sum(nums, list(depths))
            depths = np.array(depths)
    return nums, list(depths)

from math import floor, ceil
def reduce_sum_once(nums, depths):
    for i in range(len(nums)):
        if depths[i] == 4: return explode(nums, depths, i)
    for i in range(len(nums)):
        if nums[i] > 9: return split(nums, depths, i)
    return None

def explode(nums, depths, i):
    if i > 0:
        nums[i-1] += nums[i]
    if i+2 < len(nums):
        nums[i+2] += nums[i+1]
    del nums[i]
    nums[i] = 0
    del depths[i]
    depths[i] -= 1
    return nums, depths

def split(nums, depths, i):
    nums.insert(i + 1, ceil(nums[i] / 2))
    nums[i] = floor(nums[i] / 2)
    depths.insert(i + 1, depths[i] + 1)
    depths[i] += 1
    return nums, depths

def reduce_sum(nums, depths):
    while reduce_sum_once(nums, depths):
        pass
    return nums, np.array(depths)

def magnitude(nums):
    if type(nums) == list:
        return (magnitude(nums[0]) * 3) + (magnitude(nums[1]) * 2)
    else:
        return nums

def create_list(nums, depths):
    depth = -1
    string = ""
    counts = []
    for i in range(len(nums)):
        while depth < depths[i]:
            string += "["
            counts.append(0)
            depth += 1
        while depth > depths[i]:
            string += str(nums[i])
            string += ("],")
            counts.pop()
            depth -= 1
        string += (str(nums[i]) + ",")
        counts[-1] += 1
        while (counts[-1] == 2):
            string += ("],")
            counts.pop()
            if not counts:
                break
            counts[-1] += 1
            depth -= 1
    return eval(string.replace(",]", "]")[:-1])

max_mag = 0
for line1 in content.splitlines():
    for line2 in content.splitlines():
        nums, depths = parse_line(line1)
        depths = np.array(depths)
        temp_nums, temp_depths = parse_line(line2)
        nums += temp_nums
        depths += 1
        temp_depths = np.array(temp_depths)
        temp_depths += 1
        depths = np.concatenate((depths, temp_depths))
        max_mag = max(max_mag, magnitude(create_list(*reduce_sum(nums, list(depths)))))
print(max_mag)
