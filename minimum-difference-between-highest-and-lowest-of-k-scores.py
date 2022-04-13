class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        minDiff = float('inf')
        for i in range(n - k + 1):
            minDiff = min(minDiff, nums[i + k - 1] - nums[i])
        return minDiff