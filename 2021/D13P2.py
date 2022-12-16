import numpy as np
myfile = open("input.txt")
content = myfile.read()

dots = []
for line in content.splitlines():
    if not line:
        break
    dots.append(list(map(int, line.split(','))))

from itertools import chain
graph = np.zeros((np.array(dots).max(axis=0))+1)

for dot in dots:
    graph[dot[0],dot[1]] = 1

graph = graph.T

for line in content.splitlines():
    if "fold" in line:
        num = int(line.split('=')[1])
        if "x" in line:
            graph = graph[:,:num] + np.flip(graph[:,num+1:], axis=1)
        if "y" in line:
            graph = graph[:num] + graph[num+1:][::-1]

print((graph>0).sum())
graph[graph>0] = 1

for line in graph:
    print("".join(list(map(lambda x: "#" if x else ".", line))))
