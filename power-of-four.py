class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        bi = "{:b}".format(n)
        return n > 0 and bi.count("1") == 1 and bi[::-1].index("1") % 2 == 0 