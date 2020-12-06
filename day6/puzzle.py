# AoC day 6
# puzzle 1
import string


with open("input.txt") as file:
    s = set()
    entries = []
    for line in file.readlines():
        if line != '\n':
            s.update([x for x in line.strip('\n')])
        else:
            entries.append(s)
            s = set()
    entries.append(s)

# print result
print(sum([len(x) for x in entries]))

# puzzle 2
with open("input.txt") as file:
    s = set([x for x in string.ascii_lowercase])
    entries = []
    for line in file.readlines():
        if line != '\n':
            s = s.intersection([x for x in line.strip('\n')])
        else:
            entries.append(s)
            s = set([x for x in string.ascii_lowercase])
    entries.append(s)

# print result
print(sum([len(x) for x in entries]))