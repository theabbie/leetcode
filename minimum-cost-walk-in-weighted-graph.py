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
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        dsu = DSU(n)
        for u, v, w in edges:
            dsu.union(u, v)
        ands = [-1] * n
        for u, v, w in edges:
            if ands[dsu.find(u)] == -1:
                ands[dsu.find(u)] = w
            else:
                ands[dsu.find(u)] &= w
        res = []
        for u, v in query:
            if u == v:
                res.append(0)
            elif dsu.find(u) == dsu.find(v):
                res.append(ands[dsu.find(u)])
            else:
                res.append(-1)
        return res