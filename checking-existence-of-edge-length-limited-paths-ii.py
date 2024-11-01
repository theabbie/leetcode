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

class DistanceLimitedPathsExist:
    def __init__(self, n: int, edgeList: List[List[int]]):
        graph = [[] for _ in range(n)]
        edgeList.sort(key = lambda p: p[2])
        dsu = DSU(n)
        for u, v, w in edgeList:
            if dsu.find(u) != dsu.find(v):
                graph[u].append((v, w))
                graph[v].append((u, w))
                dsu.union(u, v)
        LOG = 2
        p = 1
        while p <= n:
            LOG += 1
            p *= 2
        depth = [0] * n
        parent = [[i] * LOG for i in range(n)]
        mxedge = [[float('-inf')] * LOG for i in range(n)]
        v = [False] * n
        for src in range(n):
            if v[src]:
                continue
            stack = [(src, 0, -1)]
            while stack:
                i, d, p = stack.pop()
                depth[i] = d
                v[i] = True
                for j, w in graph[i]:
                    if j != p:
                        parent[j][0] = i
                        mxedge[j][0] = w
                        stack.append((j, d + 1, i))
        for jump in range(1, LOG):
            for i in range(n):
                mxedge[i][jump] = max(mxedge[i][jump - 1], mxedge[parent[i][jump - 1]][jump - 1])
                parent[i][jump] = parent[parent[i][jump - 1]][jump - 1]
        self.dsu = dsu
        self.parent = parent
        self.mxedge = mxedge
        self.depth = depth
        self.LOG = LOG

    def query(self, p: int, q: int, limit: int) -> bool:
        if self.dsu.find(p) != self.dsu.find(q):
            return False
        bigedge = float('-inf')
        if self.depth[p] > self.depth[q]:
            p, q = q, p
        diff = self.depth[q] - self.depth[p]
        jump = 0
        while diff:
            if diff & 1:
                bigedge = max(bigedge, self.mxedge[q][jump])
                q = self.parent[q][jump]
            diff //= 2
            jump += 1
        for jump in range(self.LOG - 1, -1, -1):
            if self.parent[p][jump] != self.parent[q][jump]:
                bigedge = max(bigedge, self.mxedge[p][jump], self.mxedge[q][jump])
                p = self.parent[p][jump]
                q = self.parent[q][jump]
        if p != q:
            bigedge = max(bigedge, self.mxedge[p][0], self.mxedge[q][0])
        return bigedge < limit