import math

class Solution:
    def numSquaresRec(self, n: int) -> int:
        if n <= 1:
            return n
        if n in self.memo:
            return self.memo[n]
        root = int(math.sqrt(n))
        minSquares = float('inf')
        for k in range(1, root + 1):
            minSquares = min(minSquares, 1 + self.numSquaresRec(n - k * k))
        self.memo[n] = minSquares
        return minSquares

    def numSquares(self, n: int) -> int:
        self.memo = {}
        return self.numSquaresRec(n)