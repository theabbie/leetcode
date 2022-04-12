class Solution:
    def countSub(self, a, b):
        m = len(a)
        n = len(b)
        dp = [[0 for i in range(n + 1)] for j in range(m + 1)]
        for i in range(n + 1):
            dp[0][i] = 0
        for i in range(m + 1):
            dp[i][0] = 1
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if a[i - 1] == b[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[m][n]
    
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        n = len(text)
        mxsub = self.countSub(text, pattern)
        a = text.count(pattern[0])
        b = text.count(pattern[1])
        return mxsub + max(a, b)
        # pos = []
        # for i in range(n):
        #     if text[i] in pattern:
        #         pos.append(i)
        #         pos.append(i + 1)
        # for i in pos:
        #     for j in range(2):
        #         val = self.countSub(text[:i] + pattern[j] + text[i:], pattern)
        #         mxsub = max(mxsub, val)
        # return mxsub