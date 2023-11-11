class Solution:
    def prob(self, a, b):
        if a <= 0 and b <= 0:
            return 0.5
        if a <= 0 and b > 0:
            return 1
        if a <= 0 or b <= 0:
            return 0
        key = (a, b)
        if key in self.cache:
            return self.cache[key]
        res = 0
        for ax, bx in [(100, 0), (75, 25), (50, 50), (25, 75)]:
            res += self.prob(a - ax, b - bx)
        res /= 4
        self.cache[key] = res
        return res
    
    def soupServings(self, n: int) -> float:
        if n >= 4800:
            return 1
        self.cache = {}
        return self.prob(n, n)