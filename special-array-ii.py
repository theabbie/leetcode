class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(nums)
        dp = [1] * n
        for i in range(n - 2, -1, -1):
            if nums[i] % 2 != nums[i + 1] % 2:
                dp[i] = 1 + dp[i + 1]
        return [dp[l] >= r - l + 1 for l, r in queries]