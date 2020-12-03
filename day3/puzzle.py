# AOC day 3
# puzzle 1

# read input
with open("input.txt") as f:
    entries = [x.strip('\n') for x in f.readlines()]

# compute relevant indices
# right 3, down 1
indices = [(3*i) % len(entries[0]) for i in range(0, len(entries))]

# check for trees at index, entry
rl = [x[i] == '#' for (x, i) in zip(entries, indices)]

# print result
print(sum(rl))

# puzzle 2

# right 1, down 1
indices = [i % len(entries[0]) for i in range(0, len(entries))]
rl1 = [x[i] == '#' for (x, i) in zip(entries, indices)]

# right 5, down 1
indices = [(5 * i) % len(entries[0]) for i in range(0, len(entries))]
rl2 = [x[i] == '#' for (x, i) in zip(entries, indices)]

# right 7, down 1
indices = [(7 * i) % len(entries[0]) for i in range(0, len(entries))]
rl3 = [x[i] == '#' for (x, i) in zip(entries, indices)]

# right 1, down 2
indices = [int(i/2) % len(entries[0]) if i % 2 == 0 else -1 for i in range(0, len(entries))]
rl4 = [x[i] == '#' if i != -1 else False for (x, i) in zip(entries, indices)]

# print result
print(sum(rl) * sum(rl1) * sum(rl2) * sum(rl3) * sum(rl4))
