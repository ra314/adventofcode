content = open("input.txt").read()

import re

def get_abas(string):
  return [x[0] for x in re.findall(r'(?=((.)(?!\2).\2))', string)]

def supports_ssl(string):
  hypernet_sequences = re.findall(r'\[(\w+)\]', string)
  non_hypernet_sequences = re.sub(r'\[\w+\]', ' ', string).split()

  babs = []
  for seq in non_hypernet_sequences:
    babs.extend(get_abas(seq))

  babs2 = []
  for seq in hypernet_sequences:
    babs2.extend(get_abas(seq))

  babs2 = [x[1]+x[0]+x[1] for x in babs2]
  return len(set(babs).intersection(set(babs2))) != 0

total = 0  
for line in content.splitlines():
  total += supports_ssl(line)

print(total)


lines = [re.split(r'\[([^\]]+)\]', line) for line in open('input.txt')]
parts = [(' '.join(p[::2]), ' '.join(p[1::2])) for p in lines]
i = 0
for sn, hn in parts:
  a = supports_ssl(content.splitlines()[i])
  b = any(a == c and a != b and b+a+b in hn for a, b, c in zip(sn, sn[1:], sn[2:]))
  if a != b:
    print(content.splitlines()[i])
    print(i)
    break
  i += 1

for a, b, c in zip(sn, sn[1:], sn[2:]):
  if a == c and a != b and b+a+b in hn:
    print(a,b,c)
