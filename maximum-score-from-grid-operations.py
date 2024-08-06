class Solution:
    def maximumScore(self, grid: List[List[int]]) -> int:
        n = len(grid)
        pf = [[0] * (n + 1) for _ in range(n)]
        for j in range(n):
            for i in range(n):
                pf[j][i + 1] = pf[j][i] + grid[i][j]
        dp = [[0] * 2 for _ in range(n + 1)]
        ndp = [[0] * 2 for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for last in range(n + 1):
                for bigger in range(2):
                    for l in range(n + 1):
                        score = 0
                        if l < last:
                            score += pf[i][last] - pf[i][l]
                        elif l > last and bigger and i > 0:
                            score += pf[i - 1][l] - pf[i - 1][last]
                        ndp[last][bigger] = max(ndp[last][bigger], score + dp[l][int(l >= last)])
            dp, ndp = ndp, dp
        return max(dp[0][0], dp[0][1])