myfile = open("input2.txt")
content = myfile.read()[:-1]

import hashlib
password = list("xxxxxxxx")

j = 0
while 'x' in password:
  while True:
    hash_val = hashlib.md5((content+str(j)).encode('utf-8')).hexdigest()
    j += 1
    if hash_val[:5] == '00000':
      if hash_val[5].isdigit():
        if int(hash_val[5])<8:
          if password[int(hash_val[5])] == 'x':
            password[int(hash_val[5])] = hash_val[6]
            print("".join(password))
            break

print("".join(password))
