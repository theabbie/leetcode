class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        maxGap = float('-inf')
        n = len(nums)
        if n <= 1:
            return 0
        nums.sort()
        for i in range(1, n):
            maxGap = max(maxGap, nums[i] - nums[i - 1])
        return maxGap