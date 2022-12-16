myfile = open("input2.txt")
content = myfile.read()
content = content[:-1].split(',')

from collections import Counter

def calc_length(path):
  counts = Counter(path)
  new_counts = {}
  
  for pair in (('n','s'),('nw','se'),('sw','ne')):
    n = pair[0]
    s = pair[1]
    new_counts[n] = 0 if counts[s] > counts[n] else counts[n]-counts[s]
    new_counts[s] = 0 if counts[n] > counts[s] else counts[s]-counts[n]
  counts = new_counts

  from itertools import cycle
  dirs = cycle(['n','ne','se','s','sw','nw'])
  combinations = []
  for _ in range(6):
    triplet = []
    triplet.append(next(dirs))
    triplet.append(next(dirs))
    double_dir = triplet[-1]
    triplet.append(next(dirs))
    # Iterate 4 times to start at the next dir
    for _ in range(4):
      next(dirs)
    combinations.append((triplet, double_dir))

  for pair in combinations:
    triplet = pair[0]
    double_dir = pair[1]
    relevant_counts = [counts[t] for t in triplet]
    if min(relevant_counts)>0:
      counts[double_dir] += min(relevant_counts)
      for t in triplet:
        if t != double_dir:
          counts[t] -= min(relevant_counts)
  
  return sum(counts.values())

distances = []
for i in range(1,len(content)+1):
  distances.append(calc_length(content[:i]))

print(max(distances))
