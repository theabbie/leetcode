from collections import defaultdict

n, q = map(int, input().split())

class DSU:
    def __init__(self):
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

res = []

dsu = DSU(n)

vals = [0] * n

for i in range(q):
    a, b, d = map(int, input().split())
    a -= 1
    b -= 1
    if a > b:
        a, b = b, a
        d *= -1
    if dsu.find(a) != dsu.find(b):
        res.append(i + 1)
        dsu.merge(a, b)
    elif vals[a] - vals[b] == d:
        res.append(i + 1)

print(*res)