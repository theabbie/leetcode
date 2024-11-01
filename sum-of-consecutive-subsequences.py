from collections import Counter

class Solution:
    def getSum(self, nums: List[int]) -> int:
        M = 10 ** 9 + 7
        n = len(nums)
        def solve(arr):
            ctr = Counter()
            dp = Counter()
            res = 0
            for i in range(n - 1, -1, -1):
                curr = 1 + ctr[arr[i] + 1]
                s = arr[i] * curr + dp[arr[i] + 1]
                res += s
                ctr[arr[i]] += curr
                dp[arr[i]] += s
                res %= M
                ctr[arr[i]] %= M
                dp[arr[i]] %= M
            return res
        return (solve(nums) + solve(nums[::-1]) - sum(nums)) % M