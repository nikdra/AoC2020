# AoC day 8
# puzzle 1


# read input
with open('input.txt') as file:
    entries = [line.split() for line in file.read().splitlines()]


# function to read accumulator value in program
def boot_accumulator(code, line, visited, acc):
    if line == len(code):
        return acc
    if line in visited:
        return acc
    if code[line][0] == 'acc':
        val = int(code[line][1][1:])
        return boot_accumulator(code, line+1, visited+[line], acc + val if code[line][1][0] == '+' else acc-val)
    if code[line][0] == 'jmp':
        val = int(code[line][1][1:])
        return boot_accumulator(code, line + val if code[line][1][0] == '+' else line-val, visited+[line], acc)
    else:
        return boot_accumulator(code, line + 1, visited + [line], acc)


# print result
print(boot_accumulator(entries, 0, [], 0))


# puzzle 2
# function to find the line that should be changed
def fix_code(code, line, visited, changed):
    if line == len(code):
        return True
    if line in visited:
        return False
    if code[line][0] == 'acc':
        return fix_code(code, line+1, visited+[line], changed)
    if code[line][0] == 'jmp':
        val = int(code[line][1][1:])
        if changed:
            return fix_code(code, line + val if code[line][1][0] == '+' else line-val, visited+[line], changed)
        elif fix_code(code, line + 1, visited + [line], True):
            return line
        else:
            return fix_code(code, line + val if code[line][1][0] == '+' else line-val, visited+[line], changed)
    else:
        val = int(code[line][1][1:])
        if changed:
            return fix_code(code, line + 1, visited + [line], changed)
        elif fix_code(code, line + val if code[line][1][0] == '+' else line-val, visited+[line],  True):
            return line
        else:
            return fix_code(code, line + 1, visited + [line], changed)


# find line that should be fixed
fix_line = fix_code(entries, 0, [], False)

# change entry in code
entries[fix_line][0] = 'jmp' if entries[fix_line][0] == 'nop' else 'nop'

# print corrected result
print(boot_accumulator(entries, 0, [], 0))
