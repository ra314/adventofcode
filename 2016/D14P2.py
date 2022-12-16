myfile = open("input.txt")
content = "zpqevtbw"
#content = "abc"


import multiprocessing

try:
    cpus = multiprocessing.cpu_count()
except NotImplementedError:
    cpus = 2   # arbitrary default

import hashlib

def hash(input_str):
  hash_val = hashlib.md5((input_str).encode('utf-8')).hexdigest()
  for j in range(2016):
    hash_val = hashlib.md5((hash_val).encode('utf-8')).hexdigest()
  return hash_val

pool = multiprocessing.Pool(processes=cpus)
hashes = pool.map(hash, [content+str(num) for num in range(100000)])

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
        num_keys += 1
        print(f"Found key {num_keys} at index {k}")
        break
