# AoC day 4
# puzzle 1
import re
from functools import reduce


pattern = re.compile(r"(\w\w\w):([a-zA-Z0-9#]+)")

entries = []

# read input
with open("input.txt") as file:
    fields = []
    for line in file.readlines():
        if line != '\n':
            fields += pattern.findall(line)
        else:
            entries.append(fields)
            fields = []
    entries.append(fields)


def check_valid(passport):
    f, v = list(zip(*passport))
    if len(f) == 8 or (len(f) == 7 and 'cid' not in f):
        return 1
    return 0


rl = reduce(lambda x, y: x + check_valid(y), entries, 0)

print(rl)

# puzzle 2


def check_valider(passport):
    f, v = list(zip(*passport))
    p1 = re.compile(r"#[0-9a-f]{6}")
    p2 = re.compile(r"\d{9}")
    p3 = re.compile(r"(\d+)(\w{2})")
    if len(f) == 8 or (len(f) == 7 and 'cid' not in f):
        res = True
        for fi, va in passport:
            if fi == 'byr':
                res = res and (1920 <= int(va) <= 2002)
            elif fi == 'iyr':
                res = res and (2010 <= int(va) <= 2020)
            elif fi == 'eyr':
                res = res and (2020 <= int(va) <= 2030)
            elif fi == 'hgt':
                m = p3.fullmatch(va)
                if m is not None:
                    x, y = m.groups()
                    if y == 'cm':
                        res = res and (150 <= int(x) <= 193)
                    else:
                        res = res and (59 <= int(x) <= 76)
                else:
                    res = False
            elif fi == 'hcl':
                res = res & (p1.fullmatch(va) is not None)
            elif fi == 'ecl':
                res = res & (va in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'])
            elif fi == 'pid':
                res = res & (p2.fullmatch(va) is not None)
        return res
    return False


rl = reduce(lambda x, y: x + check_valider(y), entries, 0)

print(rl)
