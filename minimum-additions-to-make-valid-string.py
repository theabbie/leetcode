import math

class Solution:
    def LCS(self, text1, text2):
        n,m=len(text1),len(text2)
        dp=[[0]*(m+1) for _ in range(n+1)]
        for i in range(n):
            for j in range(m):
                if text1[i]==text2[j]:
                    dp[i+1][j+1]=dp[i][j]+1
                else:
                    dp[i+1][j+1]=max(dp[i][j+1],dp[i+1][j])
        return dp[-1][-1]
    
    def addMinimum(self, word: str) -> int:
        n = len(word)
        res = float('inf')
        l = math.ceil(n / 3)
        ctr = 3 + max(word.count("a"), word.count("b"), word.count("c"))
        for i in range(ctr):
            x = self.LCS("abc" * l, word)
            if x >= n:
                res = min(res, 3 * l - x)
            l += 1
        return res