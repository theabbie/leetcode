n, m, k = map(int, input().split())

edges = []

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

for _ in range(m):
    u, v, w = map(int, input().split())
    edges.append((u - 1, v - 1, w))

res = float('inf')

def find(edges, i, used, rem):
    global res
    if i >= len(edges):
        if rem == 0:
            dsu = DSU(n)
            valid = True
            curr = 0
            for j in range(len(edges)):
                if used & (1 << j):
                    if dsu.find(edges[j][0]) == dsu.find(edges[j][1]):
                        valid = False
                        break
                    curr += edges[j][2]
                    dsu.union(edges[j][0], edges[j][1])
            if valid:
                res = min(res, curr % k)
        return
    find(edges, i + 1, used, rem)
    if rem > 0:
        find(edges, i + 1, used | (1 << i), rem - 1)

find(edges, 0, 0, n - 1)

print(res)