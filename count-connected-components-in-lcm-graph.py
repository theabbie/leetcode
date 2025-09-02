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
    def countComponents(self, nums: List[int], threshold: int) -> int:
        n = len(nums)
        dsu = DSU(threshold + 1)
        for el in nums:
            mul = 1
            while el * mul <= threshold:
                dsu.union(el, el * mul)
                mul += 1
        return len(set(dsu.find(el) for el in nums if el <= threshold))  + len([el for el in nums if el > threshold])