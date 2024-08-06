M = 10 ** 9 + 7

class Solution:
    def numberOfPermutations(self, n: int, requirements: List[List[int]]) -> int:
        req = [-1] * n
        for i, c in requirements:
            req[i] = c
        K = req[-1]
        dp = [[0] * (K + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = 1
        pf = [0] * (K + 2)
        for inv in range(K + 1):
            pf[inv + 1] = pf[inv] + dp[0][inv]
            pf[inv + 1] %= M
        for i in range(1, n + 1):
            for inv in range(K + 1):
                if req[i - 1] != -1 and inv != req[i - 1]:
                    dp[i][inv] = 0
                    continue
                x = min(i, inv + 1)
                dp[i][inv] = M + pf[inv + 1] - pf[inv + 1 - x]
                dp[i][inv] %= M
            pf[0] = 0
            for inv in range(K + 1):
                pf[inv + 1] = pf[inv] + dp[i][inv]
                pf[inv + 1] %= M
        return dp[n][K]