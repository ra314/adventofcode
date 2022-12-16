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

count = 0
for sset in powerset(nums):
  if sum(sset) == 150:
    print(sset)
    count += 1
print(count)
