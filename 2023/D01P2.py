f1 = open("1in.txt", "r")
f2 = open("2in.txt", "r")
content = f2.read()

nums = 'one, two, three, four, five, six, seven, eight, nine, 1, 2, 3, 4, 5, 6, 7, 8, 9'.split(', ')
total = 0
for line in content.splitlines():
  min_index = len(line)
  min_num = -1
  for num in nums:
    index = line.find(num)
    if index == -1: continue
    if index < min_index:
      min_index, min_num = index, num
  if len(min_num) > 1:
    min_num = str(nums.index(min_num) + 1)
  #print(min_index, min_num)
  max_index = -1
  max_num = -1
  for num in nums:
    index = line.rfind(num)
    if index == -1: continue
    if index > max_index:
      max_index, max_num = index, num
  if len(max_num) > 1:
    max_num = str(nums.index(max_num) + 1)
  print(min_num, max_num)
  total += int(min_num + max_num)

print(total)


