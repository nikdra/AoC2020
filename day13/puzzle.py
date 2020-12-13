# AoC day 13
# puzzle 1
from functools import reduce

with open('input.txt') as file:
    ts = int(file.readline())
    intlist = file.readline().split(',')
    buses = list(map(int, filter(lambda x: x != 'x', intlist)))

# time to wait for next bus
wait = [x - ts % x for x in buses]

# print results
print([x * y for (x, y) in zip(buses, wait) if y == min(wait)])

# puzzle 2
ilist = [(int(x), int(x) - i) for i, x in enumerate(intlist) if x != 'x']


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


def chinese_remainder(n, a):
    p = reduce(lambda x, y: x*y, n, 1)
    total = sum(y * modinv(p // x, x) * (p // x) for x, y in zip(n, a))
    return total % p


print(chinese_remainder(*zip(*ilist)))
