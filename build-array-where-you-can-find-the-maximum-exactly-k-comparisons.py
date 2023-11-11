M = 10 ** 9 + 7

class Solution:
    def count(self, i, n, maxval, m, rem):
        if rem < 0 or rem > n - i:
            return 0
        if i >= n:
            return 1
        key = (i, maxval, rem)
        if key in self.cache:
            return self.cache[key]
        res = maxval * self.count(i + 1, n, maxval, m, rem)
        for j in range(maxval + 1, m + 1):
            res += self.count(i + 1, n, j, m, rem - 1)
            res %= M
        res %= M
        self.cache[key] = res
        return res
    
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        self.cache = {}
        return self.count(0, n, 0, m, k)