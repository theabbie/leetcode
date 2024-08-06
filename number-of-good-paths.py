from collections import *

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        
    def find(self, x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if py != px:
            self.parent[py] = px

class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        n = len(vals)
        distinct_values = sorted(set(vals))
        edgemap = defaultdict(list)
        nodemap = defaultdict(list)
        for a, b in edges:
            edgemap[max(vals[a], vals[b])].append((a, b))
        for i in range(n):
            nodemap[vals[i]].append(i)
        dsu = DSU(n)
        res = n
        for el in distinct_values:
            for a, b in edgemap[el]:
                dsu.union(a, b)
            ctr = Counter()
            for node in nodemap[el]:
                ctr[dsu.find(node)] += 1
            for parent in ctr:
                res += ctr[parent] * (ctr[parent] - 1) // 2
        return res