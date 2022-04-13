class Solution:
    def integerBreak(self, n: int) -> int:
        maxp = float('-inf')
        for k in range(2, n + 1):
            val = n // k
            p = (val ** (k - (n % k))) * ((val + 1) ** (n % k))
            maxp = max(p, maxp)
        return maxp