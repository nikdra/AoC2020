# AoC day 16
# puzzle 1
import re
from functools import reduce

# read input
with open('input.txt') as file:
    entries = [x for x in file.read().split('\n\n')]


# preprocess rules
def get_rules(line):
    lines = line.split('\n')
    pattern = re.compile(r"([\w\s]+): (\d+)-(\d+) or (\d+)-(\d+)")
    return [(g[0], list(map(int, g[1:]))) for g in [pattern.match(x).groups() for x in lines]]


# preprocess tickets
def get_tickets(line):
    lines = line.splitlines()
    return [list(map(int, x)) for x in [k.split(',') for k in lines[1:]]]


# preprocess own ticket
def get_ticket(line):
    lines = line.split('\n')
    return [int(x) for x in lines[1].split(',')]


rules = get_rules(entries[0])
other_tickets = get_tickets(entries[-1])


# check if value is valid in any field
def valid_in_any(val, rule):
    return any([r[1][0] <= val <= r[1][1] or r[1][2] <= val <= r[1][3] for r in rule])


# print result
print(sum([sum([0 if valid_in_any(y, rules) else y for y in x]) for x in other_tickets]))

# puzzle 2
# remove invalid tickets

other_tickets = [x for x in other_tickets if all([valid_in_any(y, rules) for y in x])]

print(other_tickets)


# check where the rules are valid
def valid_in(val, rule):
    return set(r[0] for r in rule if r[1][0] <= val <= r[1][1] or r[1][2] <= val <= r[1][3])


valids = [[valid_in(v, rules) for v in x] for x in other_tickets]

# greedy, iterative resolution of fields
while True:
    # find intersection of fields
    vals = [reduce(lambda a,b: a.intersection(b), [x[i] for x in valids])
            for i in range(len(other_tickets[0]))]
    # remove resolved fields (assuming no multiple solutions)
    for i, v in enumerate(vals):
        if len(v) == 1:
            for vs in valids:
                for j in range(len(vs)):
                    if i == j:
                        vs[j] = v
                    else:
                        vs[j].difference_update(v)

    # all fields assigned
    if valids[0] == vals:
        break

# print result
print(reduce(lambda a, b: a*b, [x for (x, r) in zip(get_ticket(entries[1]),
                                                    [item for sublist in vals for item in sublist])
                                if r.find("departure") != -1]))
