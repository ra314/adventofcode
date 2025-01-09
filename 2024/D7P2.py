import reader
content = reader.read()

def is_valid(curr: int, operands: list[int], target: int) -> bool:
  #print(f'curr: {curr}, operands: {operands}, target: {target}')
  if len(operands) == 0:
    return curr == target
  if curr > target:
    return False
  op = operands[0]
  valid_through_add = is_valid(curr + op, operands[1:], target)
  valid_through_mul = is_valid(curr * op, operands[1:], target)
  valid_through_concat = is_valid(int(str(curr)+str(op)), operands[1:], target)
  return valid_through_add or valid_through_mul or valid_through_concat

count = 0
total = 0
for line in content.splitlines():
  nums = line.split()
  target = int(nums[0][:-1])
  operands = list(map(int, nums[1:]))
  if is_valid(operands[0], operands[1:], target):
    count += 1
    total += target

print(count)
print(total)
