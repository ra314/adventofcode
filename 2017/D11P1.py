myfile = open("input2.txt")
content = myfile.read()
content = content[:-1].split(',')

from collections import Counter
counts = Counter(content)
new_counts = {}

for pair in (('n','s'),('nw','se'),('sw','ne')):
  n = pair[0]
  s = pair[1]
  new_counts[n] = 0 if counts[s] > counts[n] else counts[n]-counts[s]
  new_counts[s] = 0 if counts[n] > counts[s] else counts[s]-counts[n]

#eyeball it
