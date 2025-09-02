class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                dp[i] = 1 + dp[i + 1]
        beg = 1
        end = n // 2
        while beg <= end:
            mid = (beg + end) // 2
            pos = False
            for i in range(n - 2 * mid + 1):
                if dp[i] >= mid and dp[i + mid] >= mid:
                    pos = True
                    break
            if pos:
                beg = mid + 1
            else:
                end = mid - 1
        return beg - 1