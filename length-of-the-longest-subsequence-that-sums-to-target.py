class Solution:
    def longest(self, nums, i, rem):
        if rem < 0:
            return float('-inf')
        if i >= len(nums):
            if rem != 0:
                return float('-inf')
            return 0
        key = (i, rem)
        if key in self.cache:
            return self.cache[key]
        res = self.longest(nums, i + 1, rem)
        res = max(res, 1 + self.longest(nums, i + 1, rem - nums[i]))
        self.cache[key] = res
        return res
    
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        nums.sort(reverse = True)
        self.cache = {}
        res = self.longest(nums, 0, target)
        if res == float('-inf'):
            return -1
        return res