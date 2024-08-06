class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        n = len(s)
        o = s.count('1')
        return '1' * (o - 1) + '0' * (n - o) + '1'