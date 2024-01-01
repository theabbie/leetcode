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
    def gcdSort(self, nums: List[int]) -> bool:
        n = len(nums)
        M = max(nums)
        dsu = DSU(n)
        prev = {}
        for i in range(n):
            if nums[i] in prev:
                dsu.union(i, prev[nums[i]])
            else:
                prev[nums[i]] = i
        for gcd in range(2, M + 1):
            mul = 1
            pos = None
            while gcd * mul <= M:
                if gcd * mul in prev:
                    if pos != None:
                        dsu.union(prev[gcd * mul], pos)
                    else:
                        pos = prev[gcd * mul]
                mul += 1
        groups = [[] for _ in range(n)]
        for i in range(n):
            groups[dsu.find(i)].append(i)
        for i in range(n):
            groups[i].sort(key = lambda x: nums[x], reverse = True)
        res = nums[:]
        for i in range(n):
            res[i] = nums[groups[dsu.find(i)].pop()]
        return res == sorted(nums)