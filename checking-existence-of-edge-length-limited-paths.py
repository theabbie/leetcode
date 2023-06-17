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
    def distanceLimitedPathsExist(self, n, edgeList, queries):
        m = len(edgeList)
        p = len(queries)
        edgeList.sort(key = lambda e: e[2])
        dsu = DSU(n)
        res = [True] * len(queries)
        for i in range(p):
            queries[i].append(i)
        queries.sort(key = lambda q: q[2])
        i = 0
        for a, b, w, j in queries:
            while i < m and edgeList[i][2] < w:
                dsu.union(edgeList[i][0], edgeList[i][1])
                i += 1
            if dsu.find(a) != dsu.find(b):
                res[j] = False
        return res