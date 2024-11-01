class Solution:
    def selfDivisiblePermutationCount(self, n: int) -> int:
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        @lru_cache(maxsize = None)
        def count(i, mask):
            if i >= n:
                return 1
            res = 0
            for x in range(n):
                if not mask & (1 << x):
                    if gcd(x + 1, i + 1) == 1:
                        res += count(i + 1, mask | (1 << x))
            return res
        return count(0, 0)