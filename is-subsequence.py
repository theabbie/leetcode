class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n = len(s)
        i = 0
        for c in t:
            if i < n and s[i] == c:
                i += 1
        return i == n