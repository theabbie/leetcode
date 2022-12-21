class Solution:
    def count(self, s, i, n, tight, lastOne):
        if i >= n:
            return 1
        key = (i, tight, lastOne)
        if key in self.cache:
            return self.cache[key]
        res = 0
        d = 1
        if tight:
            d = int(s[i])
        for j in range(d + 1):
            if not lastOne or j != 1:
                res += self.count(s, i + 1, n, tight and j == d, j == 1)
        self.cache[key] = res
        return res
    
    def findIntegers(self, n: int) -> int:
        self.cache = {}
        b = "{:0b}".format(n)
        return self.count(b, 0, len(b), True, False)