class Solution:
    def isSame(self, a, b):
        if a == "." or b == ".":
            return True
        return a == b
    
    def isMatchRec(self, s, p, i, j, m, n):
        if i >= m:
            if j >= n:
                return True
            return j < n - 1 and p[j + 1] == "*" and self.isMatchRec(s, p, i, j + 2, m, n)
        if j >= n:
            return i >= m
        if j == n - 1 or p[j + 1] != "*":
            return self.isSame(s[i], p[j]) and self.isMatchRec(s, p, i + 1, j + 1, m, n)
        if p[j + 1] == "*":
            return self.isMatchRec(s, p, i, j + 2, m, n) or (self.isSame(s[i], p[j]) and self.isMatchRec(s, p, i + 1, j, m, n))
        return False
    
    def isMatch(self, s: str, p: str) -> bool:
        m = len(s)
        n = len(p)
        return self.isMatchRec(s, p, 0, 0, m, n)