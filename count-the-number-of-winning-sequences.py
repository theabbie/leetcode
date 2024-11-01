class Solution:
    def countWinningSequences(self, s: str) -> int:
        n = len(s)
        mp = {'FE': 1, 'EF': -1, 'WF': 1, 'FW': -1, 'EW': 1, 'WE': -1, 'FF': 0, 'EE': 0, 'WW': 0}
        dp = [[[-1, -1, -1] for _ in range(2 * n + 1)] for _ in range(n)]
        ss = 'FWE'
        M = 10 ** 9 + 7
        def count(i, diff, prev):
            if i >= n:
                if diff <= 0:
                    return 0
                return 1
            if prev != -1 and dp[i][n + diff][ss.index(prev)] != -1:
                return dp[i][n + diff][ss.index(prev)]
            res = 0
            for x in ss:
                if x != prev:
                    res += count(i + 1, diff + mp[x + s[i]], x)
                    res %= M
            if prev != -1:
                dp[i][n + diff][ss.index(prev)] = res
            return res
        return count(0, 0, -1)