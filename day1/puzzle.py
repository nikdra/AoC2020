# AOC day 1
# puzzle 1

# read input
with open("input.txt") as f:
    entries = [int(x) for x in f.readlines()]

# find the two entries that sum up to 2020
rl = [(x, y) for x in entries for y in entries if x + y == 2020]

# show results
print(rl)
print([x*y for (x, y) in rl])

# puzzle 2
rl = [(x, y, z) for x in entries for y in entries for z in entries if x + y + z == 2020]

# show results
print(rl)
print([x*y*z for (x, y, z) in rl])
