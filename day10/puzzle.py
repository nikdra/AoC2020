# AoC day 10
# puzzle 1

with open('input.txt') as file:
    entries = [int(x) for x in file.readlines()]

entries = [0] + sorted(entries)

entries.append(entries[-1] + 3)

diffs = [x - y for (x, y) in zip(entries[1:], entries[:-1])]

print(sum([x == 1 for x in diffs]) * sum([x == 3 for x in diffs]))


# puzzle 2
# It's a DAAAAAAG
class JoltGraph:

    def __init__(self, v, entries):
        self.v = v
        self.adj = [[j for j, p in enumerate(entries[i+1:], i+1) if p-3 <= entries[i]] for i in range(v)]
        self.n_paths = [0] * v

    def count_paths(self, u, d):
        if u == d:
            return 1
        else:
            if self.n_paths[u] == 0:
                self.n_paths[u] = sum(self.count_paths(c, d) for c in self.adj[u])
            return self.n_paths[u]


g = JoltGraph(len(entries), entries)
print(g.count_paths(0, len(entries)-1))
