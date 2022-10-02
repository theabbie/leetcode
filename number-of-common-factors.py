class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        k = min(a, b)
        res = 0
        for i in range(1, k + 1):
            if a % i == 0 and b % i == 0:
                res += 1
        return res