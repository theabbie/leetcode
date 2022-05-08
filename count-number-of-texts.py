class Solution:
    def ways(self, m, n):
        if m == 0:
            return 1
        if (m, n) in self.cache:
            return self.cache[(m, n)]
        ways = 0
        for i in range(1, min(m, n) + 1):
            ways += self.ways(m - i, n)
        self.cache[(m, n)] = ways
        return ways
    
    def countTexts(self, pressedKeys: str) -> int:
        self.cache = {}
        keys = [0, 0, 3, 3, 3, 3, 3, 4, 3, 4]
        n = len(pressedKeys)
        i = 0
        ways = 1
        while i < n:
            ctr = 1
            while i < n - 1 and pressedKeys[i] == pressedKeys[i + 1]:
                i += 1
                ctr += 1
            i += 1
            c = pressedKeys[i - 1]
            ways = (ways * self.ways(ctr, keys[int(c)])) % (10 ** 9 + 7)
        return ways