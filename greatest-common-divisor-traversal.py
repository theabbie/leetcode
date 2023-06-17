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
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        if nums == [1] * len(nums):
            return False
        N = 1 + max(nums)
        sp = [1] * N
        v = [False] * N
        for i in range(2, N, 2):
            sp[i] = 2
        for i in range(3, N, 2):
            if not v[i]:
                sp[i] = i
                j = i
                while j * i < N:
                    v[j * i] = True
                    sp[j * i] = i
                    j += 2
        dsu = DSU(N)
        for el in nums:
            curr = el
            while curr > 1:
                dsu.union(el, sp[curr])
                curr //= sp[curr]
        comps = set()
        for el in nums:
            comps.add(dsu.find(el))
        return len(comps) == 1