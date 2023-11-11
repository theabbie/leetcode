from collections import defaultdict, Counter

class DSU:
    def __init__(self):
        self.parent = defaultdict(lambda: -1)
        self.size = defaultdict(lambda: 1)
        
    def find(self, a):
        if self.parent[a] == -1:
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
    def groupStrings(self, words: List[str]) -> List[int]:
        dsu = DSU()
        seen = Counter()
        for w in words:
            curr = 0
            for c in w:
                c = ord(c) - ord('a')
                curr |= 1 << c
            seen[curr] += 1
        for curr in seen:
            for c in range(26):
                if not curr & (1 << c):
                    if curr | (1 << c) in seen:
                        dsu.union(curr, curr | (1 << c))
                else:
                    without = curr & ~(1 << c)
                    if without in seen:
                        dsu.union(curr, without)
                    for cc in range(26):
                        if without | (1 << cc) in seen:
                            dsu.union(curr, without | (1 << cc))
        comps = defaultdict(int)
        for el in dsu.parent:
            comps[dsu.find(el)] += seen[el]
        return [len(comps), max(comps.values())]