M = 10 ** 9 + 7

class Solution:
    def getSum(self, i, j):
        if i < 0 or j < 0:
            return 0
        if self.qsum[i][j] != None:
            return self.qsum[i][j]
        prev = self.getSum(i - 1, j - 1)
        row = self.getSum(i - 1, j)
        col = self.getSum(i, j - 1)
        res = row + col - prev
        if self.pizza[i][j] == 'A':
            res += 1
        self.qsum[i][j] = res
        return res
    
    def numapples(self, i, j, m, n) -> int:
        c = self.getSum(i + m - 1, j + n - 1)
        l = self.getSum(i + m - 1, j - 1)
        t = self.getSum(i - 1, j + n - 1)
        s = self.getSum(i - 1, j - 1)
        return c - l - t + s
    
    def count(self, i, j, m, n, rem):
        if m == 0 or n == 0 or rem == 0:
            return 1
        key = (i, j, m, n, rem)
        if key in self.cache:
            return self.cache[key]
        res = 0
        for l in range(1, m):
            if self.numapples(i, j, l, n) > 0 and self.numapples(i + l, j, m - l, n):
                res += self.count(i + l, j, m - l, n, rem - 1)
                res %= M
        for l in range(1, n):
            if self.numapples(i, j, m, l) > 0 and self.numapples(i, j + l, m, n - l):
                res += self.count(i, j + l, m, n - l, rem - 1)
                res %= M
        self.cache[key] = res
        return res
    
    def ways(self, pizza: List[str], k: int) -> int:
        m = len(pizza)
        n = len(pizza[0])
        self.cache = {}
        self.qsum = [[None for i in range(n)] for j in range(m)]
        self.pizza = pizza
        return self.count(0, 0, m, n, k - 1)