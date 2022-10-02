class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(set(nums))
        n = len(nums)
        res = 0
        i = 0
        while i < n:
            ctr = 1
            while i < n - 1 and nums[i] + 1 == nums[i + 1]:
                ctr += 1
                i += 1
            i += 1
            res = max(res, ctr)
        return res