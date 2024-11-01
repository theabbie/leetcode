class Solution:
    def minLength(self, s: str) -> int:
        while "AB" in s or "CD" in s:
            while "AB" in s:
                i = s.index("AB")
                s = s[:i] + s[i+2:]
            while "CD" in s:
                i = s.index("CD")
                s = s[:i] + s[i+2:]
        return len(s)