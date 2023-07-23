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
    def findTheString(self, lcp: List[List[int]]) -> str:
        n = len(lcp)
        dsu = DSU(n)
        for i in range(n):
            for j in range(n):
                if lcp[i][j] > 0:
                    dsu.union(i, j)
        res = []
        x = 0
        mp = {}
        for i in range(n):
            if dsu.find(i) not in mp:
                if x >= 26:
                    return ""
                mp[dsu.find(i)] = chr(ord('a') + x)
                x += 1
            res.append(mp[dsu.find(i)])
        res = "".join(res)
        for i in range(n):
            for j in range(n):
                curr = 1 + lcp[i + 1][j + 1] if i + 1 < n and j + 1 < n else 1
                if res[i] != res[j]:
                    curr = 0
                if curr != lcp[i][j]:
                    return ""
        return res