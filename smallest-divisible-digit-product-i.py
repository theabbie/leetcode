class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def prod(x):
            p = 1
            while x:
                p *= (x % 10)
                x //= 10
            return p
        while prod(n) % t != 0:
            n += 1
        return n