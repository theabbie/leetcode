class Solution:
    def shortestPalindrome(self, s: str) -> str:
        n = len(s)
        for i in range(n, 0, -1):
            if s[:i] == s[:i][::-1]:
                return s[i:][::-1] + s
        return ""