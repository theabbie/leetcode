class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        a, b, c = sorted([a, b, c])
        res = 0
        while b > 0 and c > 0:
            res += 1
            b -= 1
            c -= 1
            a, b, c = sorted([a, b, c])
        return res