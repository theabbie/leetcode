class Solution:
    def longestPrefix(self, s: str) -> str:
        n = len(s)
        for i in range(n - 1, -1, -1):
            if s.endswith(s[:i]):
                return s[:i]