class Solution:
    def msum(self, nums, i, n, sign):
        if i >= n:
            return 0
        key = (i, sign)
        if key in self.cache:
            return self.cache[key]
        a = sign * nums[i] + self.msum(nums, i + 1, n, -sign)
        b = self.msum(nums, i + 1, n, sign)
        res = max(a, b)
        self.cache[key] = res
        return res
    
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n = len(nums)
        self.cache = {}
        return self.msum(nums, 0, n, 1)