myfile = open("input2.txt")
content = myfile.read()

total = 0
for line in content.splitlines():
  line = line.split('x')
  nums = list(map(int, line))
  # Adding the main wrapping paper
  l, w, h = nums
  total += (l*w*h)
  # Adding the slack
  nums.remove(max(nums))
  total += 2*(nums[0]+nums[1])

print(total)
