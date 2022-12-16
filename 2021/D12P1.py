import numpy as np
myfile = open("input.txt")
content = myfile.read()

from collections import defaultdict
dic_map = defaultdict(set)
for line in content.splitlines():
    line = line.split('-')
    dic_map[line[0]].add(line[1])
    dic_map[line[1]].add(line[0])

def find_num_paths(curr_node, curr_path):
    num_paths = 0
    for node in dic_map[curr_node]:
        if node == "start":
            continue
        if node == "end":
            num_paths += 1
            #print(curr_path)
            continue
        if node.islower() and node in curr_path:
            continue
        num_paths += find_num_paths(node, curr_path+[node])
    return num_paths

find_num_paths('start', ['start'])
