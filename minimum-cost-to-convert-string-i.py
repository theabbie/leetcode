class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        dp = [[float('inf')] * 26 for _ in range(26)]
        for i in range(26):
            dp[i][i] = 0
        pos = lambda c: ord(c) - ord('a')
        for i in range(len(original)):
            if cost[i] < dp[pos(original[i])][pos(changed[i])]:
                dp[pos(original[i])][pos(changed[i])]  = cost[i]
        for j in range(26):
            for i in range(26):
                for k in range(26):
                    dp[i][k] = min(dp[i][k], dp[i][j] + dp[j][k])
        res = sum(dp[pos(a)][pos(b)] for a, b in zip(source, target))
        if res == float('inf'):
            res = -1
        return res