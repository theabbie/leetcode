class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        res = 0
        for _ in range(32):
            if (a % 2) | (b % 2) != c % 2:
                if a % 2 == b % 2 == 1:
                    res += 1
                res += 1
            a = a // 2
            b = b // 2
            c = c // 2
        return res