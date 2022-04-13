class Solution:
    def longestPrefix(self, s: str) -> str:
        M = len(s)
        lps = [0] * M
        l = 0
        i = 1
        while i < M:
            if s[i] == s[l]:
                l += 1
                lps[i] = l
                i += 1
            else:
                if l != 0:
                    l = lps[l-1]
                else:
                    lps[i] = 0
                    i += 1
        return s[:lps[-1]]