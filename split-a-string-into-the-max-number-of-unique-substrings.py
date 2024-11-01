class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        n = len(s)
        def dp(i, used):
            if i >= n:
                return 0
            res = 0
            for j in range(i, n):
                if s[i:j+1] not in used:
                    used.add(s[i:j+1])
                    res = max(res, 1 + dp(j + 1, used))
                    used.remove(s[i:j+1])
            return res
        return dp(0, set())