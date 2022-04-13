class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        n *= 2
        ctr = 0
        a = 1
        while a * a <= n:
            if n % a == 0:
                p, q = a, n // a
                i = (q - p - 1) // 2
                j = (p + q - 1) // 2
                if (j - i) * (i + j + 1) == n:
                    ctr += 1
            a += 1
        return ctr