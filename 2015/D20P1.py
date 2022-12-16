from functools import reduce

def factors(n):    
  return set(reduce(list.__add__, 
    ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def get_num_presents(house_number):
  visiting_elves = factors(house_number)
  gifts = sum([elf*10 for elf in visiting_elves])
  return gifts

target = 29000000
house_number = 100000
while get_num_presents(house_number) < target:
  house_number += 1
  if house_number % 100000 == 0:
    print(house_number)
print(house_number)
