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
    def areConnected(self, n: int, threshold: int, queries: List[List[int]]) -> List[bool]:
        dsu = DSU(n + 1)
        minfact = {}
        for i in range(threshold + 1, n + 1):
            mul = 1
            while i * mul <= n:
                dsu.union(i, i * mul)
                if i * mul not in minfact:
                    minfact[i * mul] = i
                else:
                    dsu.union(i, minfact[i * mul])
                mul += 1
        return [dsu.find(a) == dsu.find(b) for a, b in queries]