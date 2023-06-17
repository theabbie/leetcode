class Solution:
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a
    
    def score(self, nums, n, used, curr):
        if used + 1 == 1 << n:
            return 0
        key = (used, curr)
        if key in self.cache:
            return self.cache[key]
        res = 0
        for i in range(n):
            for j in range(i + 1, n):
                if not used & (1 << i) and not used & (1 << j):
                    res = max(res, curr * self.gcd(nums[i], nums[j]) + self.score(nums, n, used | (1 << i) | (1 << j), curr + 1))
        self.cache[key] = res
        return res
    
    def maxScore(self, nums: List[int]) -> int:
        self.cache = {}
        return self.score(nums, len(nums), 0, 1)