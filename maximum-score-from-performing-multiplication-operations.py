class Solution:
    def maxScore(self, nums, multipliers, i, j, k, m):
        if i >= m or j > k:
            return 0
        key = (i, j, k)
        if key in self.cache:
            return self.cache[key]
        a = multipliers[i] * nums[j] + self.maxScore(nums, multipliers, i + 1, j + 1, k, m)
        b = multipliers[i] * nums[k] + self.maxScore(nums, multipliers, i + 1, j, k - 1, m)
        res = max(a, b)
        self.cache[key] = res
        return res
    
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        m = len(multipliers)
        n = len(nums)
        self.cache = {}
        return self.maxScore(nums, multipliers, 0, 0, n - 1, m)