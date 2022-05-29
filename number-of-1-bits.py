class Solution:
    def hammingWeight(self, n: int) -> int:
        if n == 0:
            return 0
        return n % 2 + self.hammingWeight(n // 2)