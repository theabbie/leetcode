class Solution:
    def lastSubstring(self, s: str) -> str:
        n = len(s)
        maxSub = ""
        for i in range(n):
            maxSub = max(maxSub, s[i:])
        return maxSub