class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        res = -1
        f = {}
        for i in range(len(s)):
            if s[i] not in f:
                f[s[i]] = i
            else:
                res = max(res, i - f[s[i]] - 1)
        return res