class Solution:
    def isSame(self, a, b):
        if a == "?" or b == "?":
            return True
        return a == b
    
    def isMatchRec(self, s, p, i, j, m, n):
        if j >= n:
            return i >= m
        if i >= m:
            if j >= n:
                return True
        if (i, j) in self.cache:
            return self.cache[(i, j)]
        if i >= m:    
            res = p[j] == "*" and self.isMatchRec(s, p, i, j + 1, m, n)
            self.cache[(i, j)] = res
            return res
        if p[j] == "*":
            res = self.isMatchRec(s, p, i, j + 1, m, n) or self.isMatchRec(s, p, i + 1, j, m, n)
            self.cache[(i, j)] = res
            return res
        res = self.isSame(s[i], p[j]) and self.isMatchRec(s, p, i + 1, j + 1, m, n)
        self.cache[(i, j)] = res
        return res
    
    def isMatch(self, s: str, p: str) -> bool:
        m = len(s)
        n = len(p)
        self.cache = {}
        return self.isMatchRec(s, p, 0, 0, m, n)