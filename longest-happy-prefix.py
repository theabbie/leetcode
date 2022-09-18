class Solution:
    def longestPrefix(self, s: str) -> str:
        n = len(s)
        z = [0] * n
        d = 0
        for i in range(1, n):
            while d and s[d] != s[i]:
                d = z[d - 1]
            d += s[i] == s[d]
            z[i] = d
        return s[:z[-1]]