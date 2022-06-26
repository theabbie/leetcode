class Solution:
    def numplace(self, n, s) -> int:
        if n == 0:
            return 1
        if (n, s) in self.cache:
            return self.cache[(n, s)]
        res = 0
        if s == 0:
            res += self.numplace(n - 1, 0)
            res += 2 * self.numplace(n - 1, 1)
            res += self.numplace(n - 1, 2)
        elif s == 1:
            res += self.numplace(n - 1, 1)
            res += self.numplace(n - 1, 0)
        else:
            res += self.numplace(n - 1, 0)
        self.cache[(n ,s)] = res
        return res
    
    def countHousePlacements(self, n: int, both = True) -> int:
        self.cache = {}
        return self.numplace(n, 0) % (10 ** 9 + 7)