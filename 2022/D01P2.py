myfile = open("input2.txt")
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
print(sum(sorted(nums)[-3:]))

# Optimized
print(max([sum([int(cal) for cal in cals.split()]) for cals in content.split("\n\n")]))
print(sum(sorted([sum([int(cal) for cal in cals.split()]) for cals in content.split("\n\n")])[-3:]))
