# AoC day 15
# puzzle 1


# read input
with open('sample.txt') as file:
    nums = [int(x) for x in file.readline().split(',')]

print(nums)


def play(numbers, turn, maxturns):
    # keep a memory of the last two occurrences of a number being spoken
    spoken = {}
    last = None
    # while the game is not over
    while turn < maxturns:
        if turn < len(numbers):
            # one of the start numbers
            spoken[numbers[turn]] = (turn, turn)
            last = numbers[turn]
        elif last not in spoken.keys():
            # number has not been spoken before
            spoken[0] = (spoken[0][1], turn)
            last = 0
        else:
            # number has been spoken before
            num = spoken[last][1] - spoken[last][0]
            if num in spoken.keys():
                # new number has been spoken before
                # update last occurence
                spoken[num] = (spoken[num][1], turn)
            else:
                # new number, make a new entry
                spoken[num] = (turn, turn)
            last = num
        turn += 1
    return last


# print result
print(play(nums, 0, 2020))

# puzzle 2
print(play(nums, 0, 30000000))
