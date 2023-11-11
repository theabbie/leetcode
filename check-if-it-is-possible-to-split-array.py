class Solution:
    def check(self, p, i, j, m):
        if i == j:
            return True
        if i + 1 == j:
            return True
        key = (i, j)
        if key in self.cache:
            return self.cache[key]
        s = p[j + 1] - p[i]
        if s - (p[i + 1] - p[i]) >= m and self.check(p, i + 1, j, m):
            self.cache[key] = True
            return True
        if s - (p[j + 1] - p[j]) >= m and self.check(p, i, j - 1, m):
            self.cache[key] = True
            return True
        self.cache[key] = False
        return False
    
    def canSplitArray(self, nums: List[int], m: int) -> bool:
        n = len(nums)
        p = [0] * (n + 1)
        for i in range(n):
            p[i + 1] += p[i] + nums[i]
        self.cache = {}
        return self.check(p, 0, n - 1, m)