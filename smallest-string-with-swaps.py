from collections import defaultdict

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
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        s = list(s)
        n = len(s)
        dsu = DSU(n)
        for a, b in pairs:
            dsu.union(a, b)
        comps = defaultdict(list)
        for i in range(n):
            comps[dsu.find(i)].append(i)
        for i in range(n):
            chars = sorted([s[j] for j in comps[i]])
            k = 0
            for j in comps[i]:
                s[j] = chars[k]
                k += 1
        return "".join(s)