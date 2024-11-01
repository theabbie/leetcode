def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

gcds = [[0] * 201 for _ in range(201)]
for i in range(201):
    for j in range(201):
        gcds[i][j] = gcd(i, j)

class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        M = 10 ** 9 + 7
        n = len(nums)
        mx = max(nums)
        dp = [[0] * (mx + 1) for _ in range(mx + 1)]
        ndp = [[0] * (mx + 1) for _ in range(mx + 1)]
        for i in range(1, mx + 1):
            dp[i][i] = 1
        for i in range(n - 1, -1, -1):
            for a in range(mx + 1):
                for b in range(mx + 1):
                    ndp[a][b] = dp[a][b] + dp[gcds[a][nums[i]]][b] + dp[a][gcds[b][nums[i]]]
                    ndp[a][b] %= M
            dp, ndp = ndp, dp
        return dp[0][0]