class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        n = len(s)
        diff = []
        for i in range(n - 1):
            if ord(s[i + 1]) - ord(s[i]) == 1:
                diff.append(1)
            else:
                diff.append(0)
        m = len(diff)
        i = 0
        res = 1
        while i < m:
            ctr = 1
            while i < m - 1 and diff[i] == diff[i + 1]:
                i += 1
                ctr += 1
            i += 1
            if diff[i - 1] == 1:
                res = max(res, ctr + 1)
        return res