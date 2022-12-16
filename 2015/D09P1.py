myfile = open("input2.txt")
content = myfile.read()
from collections import defaultdict

###Parsing
dist_dict = defaultdict(dict)
for line in content.splitlines():
  line = line.split()
  dist_dict[line[0]][line[2]] = line[-1]
  dist_dict[line[2]][line[0]] = line[-1]
all_countries = list(dist_dict.keys())
n = len(all_countries)

import numpy as np
from python_tsp.exact import solve_tsp_dynamic_programming

distance_matrix = np.zeros((n,n))
for i in range(len(distance_matrix)):
  for j in range(len(distance_matrix)):
    if i == j:
      distance_matrix[i][j] = 0
      continue
    
    distance_matrix[i][j] = dist_dict[all_countries[i]][all_countries[j]]
    distance_matrix[j][i] = distance_matrix[i][j]

# Add an extra node with 0 cost to allow the code to start anywhere
zeros = np.zeros((n+1,n+1))
zeros[1:,1:] += distance_matrix
distance_matrix = zeros

permutation, distance = solve_tsp_dynamic_programming(distance_matrix)
print(int(distance))
