myfile = open("input.txt")
content = myfile.read()

nums = []
curr = 0
for line in content.splitlines():
  if line == "":
    nums.append(curr)
    curr = 0
  else:
    curr += int(line)

print(nums)
print(max(nums))
