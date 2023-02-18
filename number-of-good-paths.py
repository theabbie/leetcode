from collections import defaultdict, Counter

class Solution:
    def find(self, x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px != py:
            self.parent[py] = px
    
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        n = len(vals)
        nodemap = defaultdict(set)
        edgemap = defaultdict(set)
        for i in range(n):
            nodemap[vals[i]].add(i)
        for a, b in edges:
            edgemap[max(vals[a], vals[b])].add((min(a, b), max(a, b)))
        self.parent = list(range(n))
        res = n
        for nodeval in sorted(edgemap.keys()):
            for a, b in edgemap[nodeval]:
                self.union(a, b)
            ctr = Counter()
            for i in nodemap[nodeval]:
                ctr[self.find(i)] += 1
            for x in ctr.values():
                res += x * (x - 1) // 2
        return res