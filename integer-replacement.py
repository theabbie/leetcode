class Solution:
    def integerReplacement(self, n: int) -> int:
        if n == 1:
            return 0
        if n == 3:
            return 2
        if n & 1:
            if (n + 1) & 3 == 0:
                return 3 + self.integerReplacement((n + 1) >> 2)
            else:
                return 2 + self.integerReplacement((n - 1) >> 1)
        else:
            return 1 + self.integerReplacement(n >> 1)