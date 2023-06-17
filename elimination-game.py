class Solution:
    def find(self, n, a, b, first):
        if n == 1:
            return a + b
        if first:
            return self.find(n // 2, 2 * a, b, False)
        if n % 2 == 0:
            b -= a
        return self.find(n // 2, 2 * a, b, True)
    
    def lastRemaining(self, n: int) -> int:
        return self.find(n, 1, 0, True)