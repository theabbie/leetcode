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
    def numSimilarGroups(self, strs: List[str]) -> int:
        n = len(strs)
        m = len(strs[0])
        dsu = DSU(n)
        for i in range(n):
            for j in range(i + 1, n):
                err = 0
                for k in range(m):
                    if strs[i][k] != strs[j][k]:
                        err += 1
                if err == 0 or err == 2:
                    dsu.union(i, j)
        res = set()
        for i in range(n):
            res.add(dsu.find(i))
        return len(res)