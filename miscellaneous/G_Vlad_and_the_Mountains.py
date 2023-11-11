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
    n, m = map(int, input().split())
    h = list(map(int, input().split()))
    edges = []
    for _ in range(m):
        i, j = map(int, input().split())
        edges.append((i - 1, j - 1))
    edges.sort(key = lambda x: max(h[x[0]], h[x[1]]))
    pos = 0
    q = int(input())
    queries = []
    res = ["NO"] * q
    for i in range(q):
        a, b, e = map(int, input().split())
        queries.append((a - 1, b - 1, e, i))
    queries.sort(key = lambda x: h[x[0]] + x[2])
    dsu = DSU(n)
    for a, b, e, i in queries:
        while pos < m and max(h[edges[pos][0]], h[edges[pos][1]]) <= h[a] + e:
            dsu.union(edges[pos][0], edges[pos][1])
            pos += 1
        if dsu.find(a) == dsu.find(b):
            res[i] = "YES"
    print("\n".join(res))
    print()