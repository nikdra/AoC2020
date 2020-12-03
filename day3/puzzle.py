# AOC day 3
# puzzle 1
from functools import reduce


# count trees in a path with slope down/right
def count_trees(lines, right, down):
    indices = [int((right * i) / down) % len(lines[0]) if i % down == 0 else -1 for i in range(0, len(lines))]
    return sum([x[i] == '#' if i != -1 else False for (x, i) in zip(lines, indices)])


# read input
with open("input.txt") as f:
    entries = [x.strip('\n') for x in f.readlines()]

# right 3, down 1
rl = count_trees(entries, 3, 1)
print(rl)

# puzzle 2
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

# count trees for each slope
rl = [count_trees(entries, *s) for s in slopes]

# print result
print(reduce(lambda x, y: x * y, rl))
