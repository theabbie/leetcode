from collections import Counter

class Solution:
    def minimumSubstringsInPartition(self, s: str) -> int:
        n = len(s)
        dp = [float('inf')] * (n + 1)
        dp[n] = 0
        for i in range(n - 1, -1, -1):
            j = i
            ctr = Counter()
            ctrctr = Counter()
            while j < n:
                if ctr[s[j]] > 0:
                    ctrctr[ctr[s[j]]] -= 1
                    if ctrctr[ctr[s[j]]] == 0:
                        del ctrctr[ctr[s[j]]]
                ctr[s[j]] += 1
                ctrctr[ctr[s[j]]] += 1
                if len(ctrctr) == 1:
                    dp[i] = min(dp[i], 1 + dp[j + 1])
                j += 1
        return dp[0]