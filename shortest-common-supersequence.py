class Solution:
    def shortestCommonSupersequence(self, a: str, b: str) -> str:
        m, n = len(a), len(b)
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                dp[i][j] = 1 + dp[i+1][j+1] if a[i] == b[j] else max(dp[i+1][j], dp[i][j+1])
        i = j = 0
        aLCS = []
        bLCS = []
        while i < m and j < n:
            if a[i] == b[j]:
                aLCS.append(i)
                bLCS.append(j)
                i += 1
                j += 1
            elif dp[i+1][j] >= dp[i][j+1]:
                i += 1
            else:
                j += 1
        alcs = [-1] + aLCS + [m]
        blcs = [-1] + bLCS + [n]
        res = []
        for i in range(len(alcs) - 1):
            res.append(a[alcs[i]+1:alcs[i+1]] + b[blcs[i]+1:blcs[i+1]])
            if alcs[i+1] < m:
                res.append(a[alcs[i+1]])
        return "".join(res)