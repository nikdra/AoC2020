# AoC day 17
# puzzle 1
# three-dimensional cellular automata
# it's also growing

# read input
def read_input(n=6, three_dims=True):
    with open('input.txt') as file:
        x = 0
        y = 0
        entries = [x for x in file.read().splitlines()]
        if three_dims:
            # all we have to consider
            xmin, xmax = -n, len(entries) + n
            ymin, ymax = -n, len(entries[0]) + n
            zmin, zmax = -n, n
            pocket_dim = dict.fromkeys([(a, b, c) for a in range(xmin, xmax + 1)
                                        for b in range(ymin, ymax + 1)
                                        for c in range(zmin, zmax + 1)], '.')
            for line in entries:
                for entry in line:
                    pocket_dim[(x, y, 0)] = entry
                    y += 1
                x += 1
                y = 0
        else:
            # all we have to consider
            xmin, xmax = -n, len(entries) + n
            ymin, ymax = -n, len(entries[0]) + n
            zmin, zmax = -n, n
            wmin, wmax = -n, n
            pocket_dim = dict.fromkeys([(a, b, c, d) for a in range(xmin, xmax + 1)
                                        for b in range(ymin, ymax + 1)
                                        for c in range(zmin, zmax + 1)
                                        for d in range(wmin, wmax + 1)], '.')
            for line in entries:
                for entry in line:
                    pocket_dim[(x, y, 0, 0)] = entry
                    y += 1
                x += 1
                y = 0
    return pocket_dim


# generate all possible neighbors
directions = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1), (0, 0)]
directions = [(x, y, z) for (x, y) in directions for z in range(-1, 2)]
# remove self
directions.remove((0, 0, 0))


# update function for a given cube
def update(cube, pocket_dim, three_dims=True):
    if three_dims:
        neighbors = [(cube[0] + a, cube[1] + b, cube[2] + c) for (a, b, c) in directions]
    else:
        neighbors = [(cube[0] + a, cube[1] + b, cube[2] + c, cube[3] + d) for (a, b, c, d) in directions]
    actives = len([x for x in neighbors if pocket_dim.get(x) == '#'])
    if (pocket_dim[cube] == '.' and actives == 3) or (pocket_dim[cube] == '#' and actives in [2, 3]):
        return '#'
    else:
        return '.'


# simulate n steps of the cube
def simulate(n=6, three_dims=True):
    cubes = read_input(n, three_dims)
    while n > 0:
        updated = {}
        for c in cubes:
            updated[c] = update(c, cubes, three_dims)
        cubes = updated
        n -= 1
    return sum([1 for x in cubes.values() if x == '#'])


# print result
print(simulate(6))

# puzzle 2
# hypercubes baby
# generate all possible neighbors
directions = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1), (0, 0)]
directions = [(x, y, z, w) for (x, y) in directions for z in range(-1, 2) for w in range(-1, 2)]
# remove self
directions.remove((0, 0, 0, 0))

print(simulate(6, False))
