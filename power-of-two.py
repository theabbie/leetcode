class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and "{:b}".format(n).count("1") == 1