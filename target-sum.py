class Solution:
    def count(self, nums, i, n, curr, target):
        if i >= n:
            if 2 * curr == target:
                return 1
            return 0
        key = (i, curr)
        if key in self.cache:
            return self.cache[key]
        a = self.count(nums, i + 1, n, curr + nums[i], target)
        b = self.count(nums, i + 1, n, curr, target)
        res = a + b
        self.cache[key] = res
        return res
    
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        total = sum(nums)
        self.cache = {}
        return self.count(nums, 0, n, 0, total + target)