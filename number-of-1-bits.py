class Solution:
    def hammingWeight(self, n: int) -> int:
        return "{:b}".format(n).count("1")