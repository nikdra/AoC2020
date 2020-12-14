# AoC day 14
# puzzle 1
import re

# read input
with open("input.txt") as file:
    entries = [x.split(" = ") for x in file.read().splitlines()]

# init memory and mask
mem = {}
mask = 36 * 'X'

# for each entry, do the thing
for entry in entries:
    if entry[0] == 'mask':
        # update mask
        mask = entry[1]
    else:
        # get value to write
        result = [m if m in ('0', '1') else v for (v, m) in zip("{:036b}".format(int(entry[1])), mask)]
        # get address
        ind = re.search('mem\[(\d+)\]', entry[0]).group(1)
        # write to memory
        mem[ind] = int(''.join(result), 2)

# print result
print(sum(mem.values()))

# puzzle 2
# init memory and mask
mem = {}
mask = 36 * '0'


# get all addresses from a floating address
def get_floating_addresses(addr):
    i = addr.find('X')
    if i == -1:
        # no floating bits left, return address
        return [addr]
    # get all possible addresses with the first floating bit set
    a1 = get_floating_addresses(addr[:i] + '0' + addr[i + 1:])
    a2 = get_floating_addresses(addr[:i] + '1' + addr[i + 1:])
    # return addresses
    return a1 + a2


# for each entry, do the thing
for entry in entries:
    if entry[0] == 'mask':
        # update mask
        mask = entry[1]
    else:
        # initial memory index in binary
        ind = "{:036b}".format(int(re.search('mem\[(\d+)\]', entry[0]).group(1)))
        # apply the mask to the memory index
        float_address = ''.join([m if m in ('1', 'X') else v for (v, m) in zip(ind, mask)])
        # find all addresses and convert them to decimal
        addrs = list(map(lambda l: int(l, 2), get_floating_addresses(float_address)))
        # write to all memory addresses
        for addr in addrs:
            mem[addr] = int(entry[1])

# print result
print(sum(mem.values()))
