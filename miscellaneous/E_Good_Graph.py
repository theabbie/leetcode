from collections import defaultdict

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

n, m = map(int, input().split())

dsu = DSU(n)

graph = defaultdict(set)

for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    dsu.union(u, v)
    graph[u].add(v)
    graph[v].add(u)

k = int(input())

groups = defaultdict(set)

for _ in range(k):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    groups[dsu.find(u)].add(u)
    groups[dsu.find(v)].add(v)

print(groups)

q = int(input())

res = ["Yes"] * q

for i in range(q):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    if dsu.find(u) != dsu.find(v):
        res[i] = "No"

print("\n".join(res))