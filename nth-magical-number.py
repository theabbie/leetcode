class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        M = 10 ** 9 + 7
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        def count(x):
            return x // a + x // b - x // ((a * b) // gcd(a, b))
        beg = end = 1
        while count(end) <= n:
            end *= 2
        res = end
        while beg <= end:
            mid = (beg + end) // 2
            if count(mid) >= n:
                res = mid % M
                end = mid - 1
            else:
                beg = mid + 1
        return res