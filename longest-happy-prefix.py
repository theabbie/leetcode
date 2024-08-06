class Solution:
    def longestPrefix(self, s: str) -> str:
        n = len(s)
        for l in range(n - 1, 0, -1):
            if s[:l] == s[-l:]:
                return s[:l]
        return ""