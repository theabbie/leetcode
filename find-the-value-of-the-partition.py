class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        res = float('inf')
        for i in range(n - 1):
            res = min(res, nums[i + 1] - nums[i])
        return res