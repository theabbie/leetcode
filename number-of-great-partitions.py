class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        M = 10 ** 9 + 7
        n = len(nums)
        total = sum(nums)
        if 2 * k > total:
            return 0
        dp = [0] * k
        dp[0] = 1
        for el in nums:
            for i in range(k - el - 1, -1, -1):
                dp[i + el] += dp[i]
        res = 0
        for i in range(k):
            res += dp[i]
        return ((1 << n) - 2 * res) % M