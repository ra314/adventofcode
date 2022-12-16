import numpy as np
myfile = open("input.txt")
content = myfile.read()

og_string = content.splitlines()[0]
rules = {}
for line in content.splitlines():
    if "->" in line:
        line = line.split(" -> ")
        rules[line[0]] = line[1]

pair_counts = rules.copy()
for key in pair_counts:
    pair_counts[key] = 0

for i in range(len(og_string)-1):
    curr_window = og_string[i:i+2]
    pair_counts[curr_window] += 1

from collections import Counter
counts = Counter(og_string)

for i in range(40):
    new_pair_counts = pair_counts.copy()
    for key in new_pair_counts:
        new_pair_counts[key] = 0
    for key, value in pair_counts.items():
        part_2 = rules[key] + key[1]
        part_1 = key[0] + rules[key]
        new_pair_counts[part_1] += value
        new_pair_counts[part_2] += value
        counts[rules[key]] += value
    pair_counts = new_pair_counts.copy()

freqs = list(counts.values())
print(max(freqs)-min(freqs))
