# AoC day 7
# puzzle 1
from functools import reduce

# read input
with open('input.txt') as file:
    entries = [line.replace(' bags', '').strip('.').replace(', ', ' ')
                   .replace(' contain', '').replace('bag', '').replace('  ', ' ').strip()
               for line in file.read().splitlines()]


# map entries to outer bag, inner bag list, number of inner bags list
def entry_mapper(entry):
    if 'no other' in entry:
        return ' '.join(entry.split(' ')[0:2]), [], []
    else:
        bags = []
        numbers = []
        s = entry.split()
        for i in range(2, len(s), 3):
            bags.append(' '.join(s[i+1:i+3]))
            numbers.append(int(s[i]))
        return ' '.join(entry.split(' ')[0:2]), bags, numbers


# map entries
entries = list(map(entry_mapper, entries))


# recursive function to find the outer bags
def find_outer_bag(bags, find):
    t = [b[0] for b in bags if find in b[1]]
    if not t:
        return []
    else:
        t += reduce(lambda x, y: x + find_outer_bag(bags, y), t, [])
        return t


# print result
print(len(set(find_outer_bag(entries, 'shiny gold'))))


# puzzle 2
# recursive function to find the number of bags that have to be contained in a given bag
def number_of_bags_inside_bag(bags, bag):
    bs = [b for b in bags if bag == b[0]][0]
    if not bs[2]:
        return 0
    else:
        return sum([i + i * number_of_bags_inside_bag(bags, b) for b, i in zip(bs[1], bs[2])])


# print result
print(number_of_bags_inside_bag(entries, 'shiny gold'))
