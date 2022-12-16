#Not my work
import fileinput

lines = list(fileinput.input('input.txt'))

# set of indexes that are initially active
initial_state = set(i for i, x in enumerate(lines[0].split()[-1]) if x == '#')

# rules map a window of 5 cells to a new cell state
# (the central cell and two neighbors in each direction)
rules = dict(line.split()[::2] for line in lines[2:])

def step(state):
    result = set()
    # check all indexes in "view" of any active cells
    for i in range(min(state) - 2, max(state) + 3):
        # construct a window string like '#.##.'
        w = ''.join('#' if j in state else '.' for j in range(i - 2, i + 3))
        # check the rule for this window
        if rules[w] == '#':
            result.add(i)
    return result

# part 1
s = initial_state
# run 20 iterations
for i in range(20):
    s = step(s)
# simply sum the active indexes
print(sum(s))

# part 2
s = initial_state
p = n = 0
# run enough iterations, tracking current and previous sums
for i in range(1000):
    p = n
    s = step(s)
    n = sum(s)
# extrapolate to 50 billion
print(p + (n - p) * (50000000000 - i))
