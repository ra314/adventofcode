import numpy as np
myfile = open("input.txt")
content = myfile.read()

points = {")": 3, "]": 57, "}": 1197, ">": 25137}
brackets_dic = {"{":"}","(":")","[":"]","<":">"}

def find_mistake_location(line):
    stack = []
    for i, char in enumerate(line):
        if char in "({<[":
            stack.append(char)
        else:
            if brackets_dic[stack.pop()] != char:
                return i
    return "No Mistakes"

total = 0
for line in content.splitlines():
    mistake_location = find_mistake_location(line)
    if mistake_location != "No Mistakes":
        total += points[line[mistake_location]]

print(total)
