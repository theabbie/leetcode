class DSU:
    def __init__(self, n):
        self.p = list(range(n))
        self.sz = [1] * n
        self.history = []
        self.components = n
 
    def find(self, x):
        return x if self.p[x] == x else self.find(self.p[x])
 
    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if self.sz[a] < self.sz[b]:
            a, b = b, a
        self.history.append((self.sz, a, self.sz[a]))
        self.history.append((self.p, b, self.p[b]))
        self.history.append((self, "components", self.components))
        if a != b:
            self.p[b] = a
            self.sz[a] += self.sz[b]
            self.components -= 1
 
    def rollback(self):
        for _ in range(3):
            arr, index, old_value = self.history.pop()
            if isinstance(arr, DSU):
                setattr(arr, index, old_value)
            else:
                arr[index] = old_value

class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        dsu = DSU(n)
        g = [[] for _ in range(n)]
        for u, v in restrictions:
            g[u].append(v)
            g[v].append(u)
        res = []
        for u, v in requests:
            dsu.union(u, v)
            allowed = True
            for x, y in restrictions:
                if dsu.find(x) == dsu.find(y):
                    allowed = False
                    break
            res.append(allowed)
            if not allowed:
                dsu.rollback()
        return res