content = open("input.txt").read()

def is_valid_triangle(nums):
  A = nums[0] + nums[1] > nums[2]
  B = nums[1] + nums[2] > nums[0]
  C = nums[2] + nums[0] > nums[1]
  return A and B and C

num_valid = 0
for line in content.splitlines():
  num_valid += is_valid_triangle(list(map(int, line.strip().split())))

print(num_valid)
