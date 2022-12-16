myfile = open("input.txt")
content = "zpqevtbw"
content = "abc"

import hashlib
hashes = []
for i in range(100000):
  hash_val = hashlib.md5((content+str(i)).encode('utf-8')).hexdigest()
  hashes.append(hash_val)

import re
[i for i,j in re.findall(r"((.)\2{3,})",hashes[0])]

num_keys = 0
for k in range(100000-1000):
  matches = [i for i,j in re.findall(r"((.)\2{2,})",hashes[k])]
  if matches:
    #print(matches, k)
    for l in range(k+1, k+1001):
      if matches[0][0]*5 in hashes[l]:
        print(hashes[l])
        print(hashes[k])
        num_keys += 1
        print(f"Found key {num_keys} at index {k}")
        break
