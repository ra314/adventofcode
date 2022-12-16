import numpy as np
myfile = open("input.txt")
content = myfile.read()

og_string = content.splitlines()[0]
rules = {}
for line in content.splitlines():
    if "->" in line:
        line = line.split(" -> ")
        rules[line[0]] = line[1]

for j in range(10):
    new_string = og_string
    i = 0
    while i < len(new_string):
        curr_window = new_string[i:i+2]
        if curr_window in rules:
            replacement = curr_window[0] + rules[curr_window] + curr_window[1]
            new_string = new_string[:i] + replacement + new_string[i+2:]
            i += 2
        else:
            i += 1
    og_string = new_string

from collections import Counter
counts = Counter(new_string)
freqs = list(counts.values())
print(max(freqs)-min(freqs))
