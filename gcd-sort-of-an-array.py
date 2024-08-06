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
            
MAX = 1 + 10 ** 5

v = [False] * MAX
sp = [0] * MAX

for i in range(2, MAX, 2):
    sp[i] = 2

for i in range(3, MAX, 2):
    if not v[i]:
        sp[i] = i
        j = i
        while j * i < MAX:
            if not v[j * i]:
                v[j * i] = True
                sp[j * i] = i
            j += 2

class Solution:
    def gcdSort(self, nums: List[int]) -> bool:
        n = len(nums)
        dsu = DSU(n)
        last = {}
        for i in range(n):
            curr = nums[i]
            while curr > 1:
                dsu.union(i, last.get(sp[curr], i))
                last[sp[curr]] = i
                curr //= sp[curr]
        groups = [[] for _ in range(n)]
        for i in range(n):
            groups[dsu.find(i)].append(i)
        for i in range(n):
            groups[i].sort(key = lambda x: nums[x], reverse = True)
        res = nums[:]
        for i in range(n):
            res[i] = nums[groups[dsu.find(i)].pop()]
        return res == sorted(nums) 