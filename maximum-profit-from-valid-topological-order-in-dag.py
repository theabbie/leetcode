class Solution:
    def maxProfit(self, n, edges, score):
        pre = [0] * n
        for u, v in edges:
            pre[v] |= 1 << u
        m = 1 << n
        dp = [float('-inf')] * m
        dp[0] = 0
        for mask in range(m):
            cur = dp[mask]
            if cur < 0:
                continue
            pos = mask.bit_count() + 1
            for i in range(n):
                if not (mask >> i & 1) and (mask & pre[i]) == pre[i]:
                    nxt = mask | (1 << i)
                    dp[nxt] = max(dp[nxt], cur + score[i] * pos)
        return dp[m - 1]