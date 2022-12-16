import numpy as np
myfile = open("input.txt")
content = myfile.read()

points = {")": 3, "]": 57, "}": 1197, ">": 25137}
brackets_dic = {"{":"}","(":")","[":"]","<":">"}
autocomplete_points = {"(": 1, "[": 2, "{": 3, "<": 4}

def find_mistake(line):
    stack = []
    for i, char in enumerate(line):
        if char in "({<[":
            stack.append(char)
        else:
            if brackets_dic[stack.pop()] != char:
                return i
    return stack

totals = []
for line in content.splitlines():
    mistake = find_mistake(line)
    if type(mistake) != int:
        if len(mistake) == 0:
            continue
        stack = mistake
        mini_total = 0
        for char in stack[::-1]:
            mini_total *= 5
            mini_total += autocomplete_points[char]
        totals.append(mini_total)

print(sorted(totals)[len(totals)//2])
