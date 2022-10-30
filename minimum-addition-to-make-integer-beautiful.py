class Solution:
    def getsum(self, n):
        res = 0
        while n:
            res += n % 10
            n //= 10
        return res
    
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        prev = n
        k = 10
        while self.getsum(n) > target:
            n = n + (k - n % k)
            k *= 10
        return n - prev