class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        total = 0
        res = float('-inf')
        for i in range(n):
            total += nums[i]
            if i >= k:
                total -= nums[i - k]
            if i >= k - 1:
                res = max(res, total)
        return res / k