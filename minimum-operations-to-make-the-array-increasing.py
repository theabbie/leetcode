class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        ctr = 0
        for i in range(n - 1):
            if nums[i + 1] <= nums[i]:
                ctr += nums[i] + 1 - nums[i + 1]
                nums[i + 1] = nums[i] + 1
        return ctr