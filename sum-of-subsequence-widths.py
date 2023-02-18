class Solution:
    def sumSubseqWidths(self, nums: List[int]) -> int:
        M = 10 ** 9 + 7
        n = len(nums)
        nums.sort()
        res = 0
        powt = [1] * (n + 1)
        for i in range(1, n + 1):
            powt[i] = 2 * powt[i - 1]
            powt[i] %= M
        res = 0
        for i in range(n):
            res += nums[i] * (powt[i] - 1)
            res -= nums[i] * (powt[n - i - 1] - 1)
            res %= M
        return (M + res) % M