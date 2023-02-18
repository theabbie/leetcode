class Solution:
    def makeStringsEqual(self, s: str, target: str) -> bool:
        n = len(s)
        a, b = s.count("0"), s.count("1")
        c, d = target.count("0"), target.count("1")
        if (b > 0 and d > 0) or (a == c and b == d):
            return True
        return False