class Solution:
    def countGoodNumbers(self, n: int) -> int:
        M = 10 ** 9 + 7
        res = pow(4, n // 2, M) * pow(5, n - n // 2, M)
        return res % M