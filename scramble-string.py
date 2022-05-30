class Solution:
    def isPos(self, s1, s2, a, b, c, d):
        n = b - a
        if n == 1:
            if s1[a] == s2[c]:
                return True
            else:
                return False
        key = (a, b, c, d)
        if key in self.cache:
            return self.cache[key]
        for l in range(1, n):
            r = n - l
            if self.isPos(s1, s2, a, a + l, c, c + l) and self.isPos(s1, s2, a + l, b, d - r, d):
                self.cache[key] = True
                return True
            if self.isPos(s1, s2, a, a + l, d - l, d) and self.isPos(s1, s2, a + l, b, c, c + r):
                self.cache[key] = True
                return True
        self.cache[key] = False
        return False
    
    def isScramble(self, s1: str, s2: str) -> bool:
        n = len(s1)
        self.cache = {}
        return self.isPos(s1, s2, 0, n, 0, n)