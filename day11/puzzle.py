# AoC day 11
# puzzle 1
# cellular automata

with open("input.txt") as file:
    entries = [x for x in file.read().splitlines()]


def neighbor(ca, x, y):
    if x < 0 or x >= len(ca):
        return '.'
    if y < 0 or y >= len(ca):
        return '.'
    return ca[x][y]


def update(ca, x, y):
    neighbors = [neighbor(ca, i, j) for i in range(x-1, x+2) for j in range(y-1, y+2) if not(i == x and j == y)]
    if ca[x][y] == 'L' and not any([n == '#' for n in neighbors]):
        return '#'
    elif ca[x][y] == '#' and sum([n == '#' for n in neighbors]) >= 4:
        return 'L'
    return ca[x][y]


# begin simulation
previous = entries

while True:
    updated = [['.'] * len(entries[0]) for i in range(len(entries))]
    for x in range(len(entries)):
        for y in range(len(entries[x])):
            updated[x][y] = update(previous, x, y)

    if previous == updated:
        break
    else:
        previous = updated

# print number of occupied seat in stable configuration
print(sum([sum([x == '#' for x in entry]) for entry in updated]))


# puzzle 2
def get_visible_neighbors(ca, x, y):
    neighbors = ['.'] * 8
    # get axes
    ns = [ca[i][y] for i in range(len(ca))]
    ew = [ca[x][j] for j in range(len(ca[x]))]
    for i in range(x-1, -1, -1):
        if ns[i] != '.':
            neighbors[0] = ns[i]
            break
    for i in range(x+1, len(ns)):
        if ns[i] != '.':
            neighbors[1] = ns[i]
            break
    for j in range(y-1, -1, -1):
        if ew[j] != '.':
            neighbors[2] = ew[j]
            break
    for j in range(y+1, len(ew)):
        if ew[j] != '.':
            neighbors[3] = ew[j]
            break
    a = x-1
    b = y-1
    while a >= 0 and b >= 0:
        if ca[a][b] != '.':
            neighbors[4] = ca[a][b]
            break
        a -= 1
        b -= 1

    a = x + 1
    b = y + 1
    while a < len(ca) and b < len(ca[x]):
        if ca[a][b] != '.':
            neighbors[5] = ca[a][b]
            break
        a += 1
        b += 1

    a = x - 1
    b = y + 1
    while a >= 0 and b < len(ca[x]):
        if ca[a][b] != '.':
            neighbors[6] = ca[a][b]
            break
        a -= 1
        b += 1

    a = x + 1
    b = y - 1
    while a < len(ca) and b >= 0:
        if ca[a][b] != '.':
            neighbors[7] = ca[a][b]
            break
        a += 1
        b -= 1

    return neighbors


def update_1(ca, x, y):
    neighbors = get_visible_neighbors(ca, x, y)
    if ca[x][y] == 'L' and not any([n == '#' for n in neighbors]):
        return '#'
    elif ca[x][y] == '#' and sum([n == '#' for n in neighbors]) >= 5:
        return 'L'
    return ca[x][y]


# begin simulation
previous = entries

while True:
    updated = [['.'] * len(entries[0]) for i in range(len(entries))]
    for x in range(len(entries)):
        for y in range(len(entries[x])):
            updated[x][y] = update_1(previous, x, y)

    if previous == updated:
        break
    else:
        previous = updated

# print number of occupied seat in stable configuration
print(sum([sum([x == '#' for x in entry]) for entry in updated]))
