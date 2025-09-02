class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.diameters = [(i, i) for i in range(n)]
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
    def diameter(self, edges):
        n = len(edges) + 1
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        depth = [0] * n
        LOG = 18
        p = [[i] * LOG for i in range(n)]
        stack = [(0, -1, 0)]
        while stack:
            i, pr, d = stack.pop()
            depth[i] = d
            for j in graph[i]:
                if j != pr:
                    p[j][0] = i
                    stack.append((j, i, d + 1)) 
        for l in range(1, LOG):
            for i in range(n):
                p[i][l] = p[p[i][l - 1]][l - 1]
        dsu = DSU(n)
        ldiameter = 0    
        def addEdge(u, v):
            nonlocal ldiameter
            l = max(dsu.diameters[dsu.find(u)], key = lambda x: getDist(u, x))
            r = max(dsu.diameters[dsu.find(v)], key = lambda x: getDist(v, x))
            first, last = max([(l, r), dsu.diameters[dsu.find(u)], dsu.diameters[dsu.find(v)]], key = lambda e: getDist(e[0], e[1]))
            dsu.union(u, v)
            dsu.diameters[dsu.find(u)] = (first, last)
            ldiameter = max(ldiameter, getDist(first, last))   
        def getDist(u, v):
            res = depth[u] + depth[v]
            if depth[u] > depth[v]:
                u, v = v, u
            diff = depth[v] - depth[u]
            jump = 0
            while diff:
                if diff & 1:
                    v = p[v][jump]
                jump += 1
                diff //= 2
            for jump in range(LOG - 1, -1, -1):
                if p[u][jump] != p[v][jump]:
                    u = p[u][jump]
                    v = p[v][jump]
            LCA = p[u][0] if u != v else u
            res -= 2 * depth[LCA]
            return res
        for u, v in edges:
            addEdge(u, v)
        return ldiameter
 
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        a = self.diameter(edges1)
        b = self.diameter(edges2)
        return max(a, b, (a + 1) // 2 + (b + 1) // 2 + 1)