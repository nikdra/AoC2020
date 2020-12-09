# AoC day 9
# puzzle 1

# read input
with open("input.txt") as file:
    entries = [int(x) for x in file.readlines()]

# set sliding window size
k = 25

# set result variable
val = None

# find first entry that is not the sum of the previous k entries
for i, x in enumerate(entries[k:], start=k):
    if not any([x == y + z for y in entries[i-k:i] for z in entries[i-k:i]]):
        # store result
        val = x
        break

# print result
print(val)

res = None

# puzzle 2
# find contiguous set of at least two numbers in our list that add up to val
for i in range(len(entries)):
    j = 2
    while i+j < len(entries) and sum(entries[i:i+j]) <= val:
        j += 1
    if j >= 3 and sum(entries[i:i+j-1]) == val:
        res = min(entries[i:i+j-1]) + max(entries[i:i+j-1])
        break

# print result
print(res)
