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
    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        res = -1
        dsu = DSU(n)
        curr = [0] * n
        ctr = 0
        for i in range(n):
            pos = arr[i] - 1
            if pos - 1 >= 0 and curr[pos - 1] == 1:
                if dsu.size[dsu.find(pos - 1)] == m:
                    ctr -= 1
                dsu.union(pos, pos - 1)
            if pos + 1 < n and curr[pos + 1] == 1:
                if dsu.size[dsu.find(pos + 1)] == m:
                    ctr -= 1
                dsu.union(pos, pos + 1)
            curr[pos] = 1
            if dsu.size[dsu.find(pos)] == m:
                ctr += 1
            if ctr > 0:
                res = i + 1
        return res