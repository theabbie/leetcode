class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        if left == 0 or right == 0:
            return 0
        a = "{:b}".format(left)
        b = "{:b}".format(right)
        if len(a) != len(b):
            return 0
        res = 1 << len(a) - 1
        return res + self.rangeBitwiseAnd(left - res, right - res)