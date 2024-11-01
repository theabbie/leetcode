MAX = 1 + 10 ** 5

v = [False] * MAX
sp = [0] * MAX

for i in range(2, MAX, 2):
    sp[i] = 2

for i in range(3, MAX, 2):
    if not v[i]:
        sp[i] = i
        j = i
        while j * i < MAX:
            if not v[j * i]:
                v[j * i] = True
                sp[j * i] = i
            j += 2
            
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

class Solution:
    def countPaths(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n + 1)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        dsu = DSU(n + 1)
        for u, v in edges:
            if sp[u] != u and sp[v] != v:
                dsu.union(u, v)
        res = 0
        for i in range(1, n + 1):
            if sp[i] != i:
                continue
            ctr = 0
            for j in graph[i]:
                if sp[j] != j:
                    res += dsu.size[dsu.find(j)] * (ctr + 1)
                    ctr += dsu.size[dsu.find(j)]
        return res