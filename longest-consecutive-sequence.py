class Solution:
    def find(self, a):
        if self.parent[a] == a:
            return a
        self.parent[a] = self.find(self.parent[a])
        return self.parent[a]

    def union(self, a, b):
        u = self.find(a)
        v = self.find(b)
        if u != v:
            self.parent[v] = u
            self.ctr[u] += self.ctr[v]
    
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        vals = set(nums)
        self.parent = {}
        self.ctr = {}
        for el in vals:
            self.parent[el] = el
            self.ctr[el] = 1
        for el in vals:
            if el - 1 in vals:
                self.union(el - 1, el)
        return max(self.ctr.values())