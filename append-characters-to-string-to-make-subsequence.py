class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        m = len(s)
        n = len(t)
        i = 0
        for j in range(m):
            if i < n and s[j] == t[i]:
                i += 1
        return n - i