class Solution:
    def maxScore(self, nums: List[int], x: int) -> int:
        n = len(nums)
        maxeven = float('-inf')
        maxodd = float('-inf')
        for i in range(n - 1, 0, -1):
            if nums[i] & 1:
                maxodd = max(maxodd, nums[i], nums[i] + maxodd, nums[i] - x + maxeven)
            else:
                maxeven = max(maxeven, nums[i], nums[i] + maxeven, nums[i] - x + maxodd)
        if nums[0] & 1:
            return max(nums[0], nums[0] + maxodd, nums[0] - x + maxeven)
        return max(nums[0], nums[0] + maxeven, nums[0] - x + maxodd)