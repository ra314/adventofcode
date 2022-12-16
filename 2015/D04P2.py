myfile = open("input2.txt")
content = "yzbqklnj"
#content = "abcdef"

import hashlib
password = ""

j = 1
while True:
  hash_val = hashlib.md5((content+str(j)).encode('utf-8')).hexdigest()
  if hash_val[:6] == '000000':
    print(j)
    break
  j += 1
