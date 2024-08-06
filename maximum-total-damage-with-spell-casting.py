from collections import *

class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        ctr = defaultdict(int)
        for el in power:
            ctr[el] += el
        dp = defaultdict(int)
        vals = sorted(ctr.items())
        i = 0
        mx = 0
        for x, val in vals:
            while i < len(vals) and vals[i][0] < x - 2:
                mx = max(mx, dp[vals[i][0]])
                i += 1
            dp[x] = val + mx
        if len(dp) == 0:
            return 0
        return max(dp.values())