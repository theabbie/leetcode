class Solution:
    def isValid(self, s: str) -> bool:
        while "abc" in s:
            i = s.index("abc")
            s = s[:i] + s[i+3:]
        return s == ""