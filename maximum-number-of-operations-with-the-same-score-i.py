class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        i = 0
        while i < n - 1 and nums[i] + nums[i + 1] == nums[0] + nums[1]:
            i += 2
            res += 1
        return res