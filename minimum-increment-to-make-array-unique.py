class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        nums.sort()
        for i in range(1, n):
            if nums[i] <= nums[i - 1]:
                res += nums[i - 1] + 1 - nums[i]
                nums[i] = nums[i - 1] + 1
        return res