class Solution:
    def newInteger(self, n: int) -> int:
        d = []
        while n:
            d.append(n % 9)
            n //= 9
        d.reverse()
        res = 0
        for x in d:
            res = 10 * res + x
        return res