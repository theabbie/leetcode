class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        x = 0
        res = 0
        for i in range(len(nums)):
            if i == 0 or nums[i] <= nums[i - 1]:
                x = nums[i]
            else:
                x += nums[i]
            res = max(res, x)
        return res