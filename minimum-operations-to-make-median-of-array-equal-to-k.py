class Solution:
    def minOperationsToMakeMedianK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        median = n // 2
        res = 0
        res += abs(nums[median] - k)
        for i in range(median):
            if nums[i] > k:
                res += nums[i] - k
        for i in range(median + 1, n):
            if nums[i] < k:
                res += k - nums[i]
        return res