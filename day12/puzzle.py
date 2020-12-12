# AoC day 12
# puzzle 1

# read input
with open('input.txt') as file:
    entries = [(x[0], int(x[1:]) if x[0] not in ("S", "W") else -int(x[1:])) for x in file.readlines()]

# our ship
ship = {
    "pos": [0, 0],
    "direction": "E"
}


def move_east_west(ship, value):
    ship["pos"][1] += value


def move_north_south(ship, value):
    ship["pos"][0] += value


def rotate_right(ship, value):
    rotations = {
        "N": "E",
        "E": "S",
        "S": "W",
        "W": "N"
    }
    while value > 0:
        ship["direction"] = rotations[ship["direction"]]
        value -= 90


def rotate_left(ship, value):
    rotations = {
        "E": "N",
        "S": "E",
        "W": "S",
        "N": "W"
    }
    while value > 0:
        ship["direction"] = rotations[ship["direction"]]
        value -= 90


def move_forward(ship, value):
    if ship["direction"] == "E":
        ship["pos"][1] += value
    elif ship["direction"] == "W":
        ship["pos"][1] -= value
    elif ship["direction"] == "N":
        ship["pos"][0] += value
    else:
        ship["pos"][0] -= value


movements = {
    "N": move_north_south,
    "S": move_north_south,
    "E": move_east_west,
    "W": move_east_west,
    "L": rotate_left,
    "R": rotate_right,
    "F": move_forward
}

# move the ship
for entry in entries:
    movements[entry[0]](ship, entry[1])

# print resulting manhattan distance
print(sum([abs(x) for x in ship["pos"]]))

# our ship
ship = {
    "pos": [0, 0],
    "waypoint": [1, 10]
}


def move_east_west_waypoint(ship, value):
    ship["waypoint"][1] += value


def move_north_south_waypoint(ship, value):
    ship["waypoint"][0] += value


def rotate_right_waypoint(ship, value):
    while value > 0:
        vec = ship["waypoint"]
        ship["waypoint"] = [-vec[1], vec[0]]
        value -= 90


def rotate_left_waypoint(ship, value):
    while value > 0:
        vec = ship["waypoint"]
        ship["waypoint"] = [vec[1], -vec[0]]
        value -= 90


def move_forward_waypoint(ship, value):
    ship["pos"][0] += value * ship["waypoint"][0]
    ship["pos"][1] += value * ship["waypoint"][1]


movements = {
    "N": move_north_south_waypoint,
    "S": move_north_south_waypoint,
    "E": move_east_west_waypoint,
    "W": move_east_west_waypoint,
    "L": rotate_left_waypoint,
    "R": rotate_right_waypoint,
    "F": move_forward_waypoint
}

# move the ship
for entry in entries:
    movements[entry[0]](ship, entry[1])

# print resulting manhattan distance
print(sum([abs(x) for x in ship["pos"]]))
