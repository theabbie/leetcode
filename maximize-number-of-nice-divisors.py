M = 10 ** 9 + 7

class Solution:
    def maxNiceDivisors(self, primeFactors: int) -> int:
        res = 1
        while primeFactors >= 2 and primeFactors % 3 != 0:
            primeFactors -= 2
            res *= 2
            res %= M
        res *= pow(3, primeFactors // 3, M)
        res %= M
        return res