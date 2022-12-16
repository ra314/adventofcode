myfile = open("input2.txt")
content = myfile.read()

nums = [int(line) for line in content.splitlines()]

def powerset(seq):
    """
    Returns all the subsets of this set. This is a generator.
    """
    if len(seq) <= 1:
        yield seq
        yield []
    else:
        for item in powerset(seq[1:]):
            yield [seq[0]]+item
            yield item

min_size = len(nums)
count = 0
ssets = []
for sset in powerset(nums):
  if sum(sset) == 150:
    ssets.append(sset)
count = sum([len(x) == 4 for x in ssets])
print(count)
