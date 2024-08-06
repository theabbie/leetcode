from collections import defaultdict

class Solution:
    def maxops(self, nums, i, j, s):
        res = 0
        if i >= j:
            return 0
        key = (i, j, s)
        if key in self.cache:
            return self.cache[key]
        if s == -1 or nums[i] + nums[j] == s:
            res = max(res, 1 + self.maxops(nums, i + 1, j - 1, s if s != -1 else nums[i] + nums[j]))
        if s == -1 or nums[i] + nums[i + 1] == s:
            res = max(res, 1 + self.maxops(nums, i + 2, j, s if s != -1 else nums[i] + nums[i + 1]))
        if s == -1 or nums[j - 1] + nums[j] == s:
            res = max(res, 1 + self.maxops(nums, i, j - 2, s if s != -1 else nums[j - 1] + nums[j]))
        self.cache[key] = res
        return res
    
    def maxOperations(self, nums: List[int]) -> int:
        n = len(nums)
        self.cache = {}
        return self.maxops(nums, 0, n - 1, -1)