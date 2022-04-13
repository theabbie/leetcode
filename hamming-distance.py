class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return "{:b}".format(x ^ y).count("1")