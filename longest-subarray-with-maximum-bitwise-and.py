class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        v = max(nums)
        res = 0
        i = 0
        while i < n:
            ctr = 1
            while i < n - 1 and nums[i] == nums[i + 1]:
                ctr += 1
                i += 1
            i += 1
            if nums[i - 1] == v:
                res = max(res, ctr)
        return res