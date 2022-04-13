class Solution:
    def numberOfMatches(self, n: int) -> int:
        matches = 0
        while n > 1:
            if n % 2 == 1:
                matches += (n - 1) // 2
                n = 1 + (n - 1) // 2
            else:
                matches += n // 2
                n = n // 2
        return matches