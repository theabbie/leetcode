class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        res = 0
        while i < n:
            curr = nums[i]
            while i < n - 1 and nums[i] < nums[i + 1]:
                i += 1
                curr += nums[i]
            res = max(res, curr)
            i += 1
        return res