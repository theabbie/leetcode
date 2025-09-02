class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        res = 0
        while len(set(nums)) != len(nums):
            nums = nums[3:]
            res += 1
        return res