from collections import defaultdict

t = int(input())

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        
    def find(self, a):
        if a == self.parent[a]:
            return a
        self.parent[a] = self.find(self.parent[a])
        return self.parent[a]
        
    def union(self, a, b):
        parent_a = self.find(a)
        parent_b = self.find(b)
        if parent_a != parent_b:
            if self.size[parent_a] < self.size[parent_b]:
                parent_a, parent_b = parent_b, parent_a
            self.parent[parent_b] = parent_a
            self.size[parent_a] += self.size[parent_b]

for _ in range(t):
    n = int(input())
    pairs = []
    dsu = DSU(n)
    for _ in range(n):
        u, v = map(int, input().split())
        pairs.append((u, v))
    for i in range(n):
        for j in range(i + 1, n):
            a, b = pairs[i]
            c, d = pairs[j]
            if max(a, c) <= min(b, d):
                dsu.union(i, j)
    res = 0
    ctr = [0] * n
    comps = defaultdict(set)
    for i in range(n):
        comps[dsu.find(i)].add(i)
    print(comps)
    for i in comps:
        if dsu.size[i] > 2:
            for j in comps[i]:
                ctr[j] += 1
        if dsu.size[i] < 2:
            res += dsu.size[i]
    deletes = set()
    for i in comps:
        if dsu.size[i] > 2:
            mx = (-1, -1)
            for j in comps[i]:
                mx = max(mx, (ctr[j], j))
            if mx[1] not in deletes:
                deletes.add(mx[1])
                res += 1
    print(res)