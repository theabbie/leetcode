class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        n = len(s)
        vals = []
        i = 0
        while i < n:
            ctr = 1
            while i < n - 1 and s[i] == s[i + 1]:
                i += 1
                ctr += 1
            i += 1
            vals.append(ctr)
        m = len(vals)
        res = 0
        for i in range(m - 1):
            res += min(vals[i], vals[i + 1])
        return res