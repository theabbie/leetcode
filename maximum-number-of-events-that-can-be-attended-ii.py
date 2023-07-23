from collections import defaultdict

class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        n = len(events)
        events.sort(key = lambda e: e[1])
        mp = {}
        for a, b, p in events:
            mp[a] = mp[b + 1] = 0
        for i, el in enumerate(sorted(mp)):
            mp[el] = i
        lefts = defaultdict(set)
        for a, b, p in events:
            lefts[mp[b + 1]].add((mp[a], p))
        dp = [[0] * (len(mp) + 1) for _ in range(k + 1)]
        for i in range(1, k + 1):
            for j in range(len(mp) + 1):
                if j > 0:
                    dp[i][j] = dp[i][j - 1]
                for l, p in lefts[j]:
                    dp[i][j] = max(dp[i][j], dp[i - 1][l] + p)
        return max(dp[k])