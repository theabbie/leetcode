class Solution:
    def countVowelPermutation(self, n: int) -> int:
        trans = [[1], [0, 2], [0, 1, 3, 4], [2, 4], [0]]
        dp = [[int(i == 0)] * 5 for i in range(n)]
        for i in range(1, n):
            for j in range(5):
                for k in trans[j]:
                    dp[i][j] += dp[i - 1][k]
        return sum(dp[n - 1]) % (10 ** 9 + 7)