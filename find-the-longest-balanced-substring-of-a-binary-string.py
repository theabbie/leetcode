class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        n = len(s)
        res = 0
        vals = []
        i = 0
        while i < n:
            ctr = 1
            while i < n - 1 and s[i] == s[i + 1]:
                ctr += 1
                i += 1
            vals.append((s[i], ctr))
            i += 1
        for i in range(len(vals) - 1):
            if vals[i][0] == '0' and vals[i + 1][0] == '1':
                res = max(res, 2 * min(vals[i][1], vals[i + 1][1]))
        return res