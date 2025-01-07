import reader
content = reader.read()

nums1 = []
nums2 = []

for line in content.splitlines():
  n1, n2 = list(map(int, line.split()))
  nums1.append(n1)
  nums2.append(n2)

nums1, nums2 = sorted(nums1), sorted(nums2)

total = 0
for n1, n2 in zip(nums1, nums2):
  total += abs(n1-n2)

print(total)

# Cleaned up solution.
nums1 = [int(line.split()[0]) for line in content.splitlines()]
nums2 = [int(line.split()[-1]) for line in content.splitlines()]
nums1, nums2 = sorted(nums1), sorted(nums2)
total = sum([abs(n1-n2) for n1, n2 in zip(nums1, nums2)])
print(total)
