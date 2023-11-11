class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        o = s.count("1")
        return "1" * (o - 1) + "0" * (len(s) - o) + "1"