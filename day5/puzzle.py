# AOC day 5
# puzzle 1


# read input
# seat rows are just a binary to decimal translation
# FBFBBFF -> 0101100 -> 44
# seat columns are just a binary to decimal translation
# RLR -> 101 -> 5
with open("input.txt") as f:
    entries = [''.join(list(map(lambda l: '1' if l in ('B', 'R') else '0', x.strip('\n')))) for x in f.readlines()]

# sort decimal ids ascending
ids = sorted([int(x[0:7], 2) * 8 + int(x[7:], 2) for x in entries])

# print maximum seat ID
print(ids[-1])

# puzzle 2
# theoretical sum of ids
# see: https://math.stackexchange.com/questions/2713656/how-to-calculate-sum-of-the-integers-from-m-to-n
s = int(((ids[0] + ids[-1]) * (ids[-1] - ids[0] + 1)) / 2)

# print missing id
print(s - sum(ids))
