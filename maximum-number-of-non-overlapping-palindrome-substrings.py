class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        smallestpalodd = [[float('-inf'), float('inf')] for i in range(n)]
        smallestpaleven = [[float('-inf'), float('inf')] for i in range(n)]
        for i in range(n):
            x, y, p = i, i, 1
            l = 0
            while x - l >= 0 and y + l < n and s[x - l] == s[y + l]:
                l += 1
                if 2 * (l - 1) + p >= k:
                    if y + l < smallestpalodd[i][1]:
                        smallestpalodd[i][0] = x - l + 1
                        smallestpalodd[i][1] = y + l
                    break
        for i in range(n):
            x, y, p = i, i + 1, 2
            l = 0
            while x - l >= 0 and y + l < n and s[x - l] == s[y + l]:
                l += 1
                if 2 * (l - 1) + p >= k:
                    if y + l < smallestpaleven[i][1]:
                        smallestpaleven[i][0] = x - l + 1
                        smallestpaleven[i][1] = y + l
                    break
        dp = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if smallestpalodd[j][1] <= n and smallestpalodd[j][0] >= i:
                    dp[i] = max(dp[i], 1 + dp[smallestpalodd[j][1]])
                if smallestpaleven[j][1] <= n and smallestpaleven[j][0] >= i:
                    dp[i] = max(dp[i], 1 + dp[smallestpaleven[j][1]])
        return dp[0]