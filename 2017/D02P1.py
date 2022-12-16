#Started 16/02/2021 13:25
#Ended 16/02/2021 13:28

myfile = open("input.txt")
content = myfile.read()

checksum = 0
for line in content.splitlines():
  nums = list(map(int, line.split()))
  checksum += (max(nums) - min(nums))

print(checksum)
