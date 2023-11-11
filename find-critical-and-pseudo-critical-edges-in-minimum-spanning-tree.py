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
    def MST(self, n, edges, skip, force):
        dsu = DSU(n)
        cost = 0
        if force != -1:
            dsu.union(edges[force][0], edges[force][1])
            cost += edges[force][2]
        for i in range(len(edges)):
            if i == skip:
                continue
            if dsu.find(edges[i][0]) == dsu.find(edges[i][1]):
                continue
            cost += edges[i][2]
            dsu.union(edges[i][0], edges[i][1])
        for i in range(n):
            if dsu.find(i) != dsu.find(0):
                cost = float('inf')
                break
        return cost
    
    def findCriticalAndPseudoCriticalEdges(self, n, edges):
        res = [[], []]
        for i in range(len(edges)):
            edges[i].append(i)
        edges.sort(key = lambda x: x[2])
        mst = self.MST(n, edges, -1, -1)
        for i in range(len(edges)):
            cost = self.MST(n, edges, i, -1)
            if cost > mst:
                res[0].append(edges[i][3])
                continue
            cost = self.MST(n, edges, i, i)
            if cost == mst:
                res[1].append(edges[i][3])
        return res