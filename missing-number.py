class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)
        for i, el in enumerate(nums):
            res ^= el ^ i
        return res