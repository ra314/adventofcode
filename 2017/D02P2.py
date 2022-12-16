#Started 16/02/2021 13:25
#Ended 16/02/2021 13:28

myfile = open("input.txt")
content = myfile.read()

checksum = 0
for line in content.splitlines():
  nums = list(map(int, line.split()))
  for i in range(len(nums)):
    for j in range(len(nums)):
      if i == j:
        continue
      if nums[i]%nums[j] == 0:
        checksum += (nums[i]/nums[j])

print(checksum)
