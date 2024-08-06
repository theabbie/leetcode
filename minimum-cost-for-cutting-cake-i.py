class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        dp = [[[[-1] * (n + 1) for _ in range(m + 1)] for _ in range(n + 1)] for _ in range(m + 1)]
        def cost(i, j, w, h):
            if w == 1 and h == 1:
                return 0
            if dp[i][j][w][h] != -1:
                return dp[i][j][w][h]
            res = float('inf')
            for x in range(1, w):
                res = min(res, cost(i, j, x, h) + cost(i + x, j, w - x, h) + horizontalCut[i + x - 1])
            for y in range(1, h):
                res = min(res, cost(i, j, w, y) + cost(i, j + y, w, h - y) + verticalCut[j + y - 1])
            dp[i][j][w][h] = res
            return res
        return cost(0, 0, m, n)