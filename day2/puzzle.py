# AOC day2
# puzzle 1
import re


# read input
with open("input.txt") as f:
    pattern = re.compile(r"(\d+)-(\d+) (\w): (\w+)")
    entries = [pattern.match(x).groups() for x in f.readlines()]

# check passwords
rl = [int(x) <= w.count(z) <= int(y) for (x, y, z, w) in entries]

# print number of correct passwords
print(sum(rl))

# puzzle 2
# check passwords
rl = [(z == w[int(x)-1]) != (z == w[int(y)-1]) for (x, y, z, w) in entries]

# print number of correct passwords
print(sum(rl))