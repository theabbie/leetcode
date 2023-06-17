from collections import Counter, defaultdict

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
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        n = len(vals)
        m = len(edges)
        dsu = DSU(n)
        for e in edges:
            e.append(max(vals[e[0]], vals[e[1]]))
        nodes = defaultdict(set)
        for i in range(n):
            nodes[vals[i]].add(i)
        edges.sort(key = lambda e: e[2])
        res = n
        i = 0
        for nodeval in sorted(set(vals)):
            while i < m and edges[i][2] <= nodeval:
                dsu.union(edges[i][0], edges[i][1])
                i += 1
            ctr = Counter()
            for x in nodes[nodeval]:
                res += ctr[dsu.find(x)]
                ctr[dsu.find(x)] += 1
        return res