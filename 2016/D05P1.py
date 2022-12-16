myfile = open("input2.txt")
content = myfile.read()[:-1]

import hashlib
password = ""

j = 0
for i in range(8):
  while True:
    hash_val = hashlib.md5((content+str(j)).encode('utf-8')).hexdigest()
    j += 1
    if hash_val[:5] == '00000':
      password += hash_val[5]
      break
    

print(password)
