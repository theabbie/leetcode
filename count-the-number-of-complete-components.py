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

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)
        for a, b in edges:
            dsu.union(a, b)
        components = defaultdict(set)
        for i in range(n):
            components[dsu.find(i)].add(i)
        res = 0
        for i in components:
            m = len(components[i])
            e = 0
            for a, b in edges:
                if dsu.find(a) == dsu.find(b) == i:
                    e += 1
            if e == m * (m - 1) // 2:
                res += 1
        return res