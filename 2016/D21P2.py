import numpy as np
from math import sqrt

myfile = open("input2.txt")
content = myfile.read()

import collections
password = 
password = collections.deque("abcdefgh")

import itertools
list(itertools.permutations([1, 2, 3]))


for 
for line in content.splitlines()[::-1]:
  line = line.split()
  if line[0] == "swap":
    if line[1] == "position":
      j = int(line[2])
      i = int(line[5])
    if line[1] == "letter":
      j = password.index(line[2])
      i = password.index(line[5])
    
    tmp = password[i]
    password[i] = password[j]
    password[j] = tmp
    
  if line[0] == "reverse":
    i = int(line[2])
    j = int(line[4])
    password = list(password)
    password[i:j+1] = password[i:j+1][::-1]
    password = collections.deque(password)
  
  if line[0] == "move":
    i = int(line[2])
    j = int(line[5])
    char = password[i]
    del password[i]
    password.insert(j, char)
  
  if line[0] == "rotate":
    if line[1] == "based":
      i = password.index(line[-1])
      password.rotate(-1)
      password.rotate(-i)
      if i>=4:
        password.rotate(-1)
    if line[1] == "right":
      password.rotate(-int(line[2]))
    if line[1] == "left":
      password.rotate(int(line[2]))
   
