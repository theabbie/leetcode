class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        res = 0
        pw = 1
        for b in range(32):
            r = 2 * pw * math.ceil((left + 1) / (pw * 2))
            if left & pw and r > right:
                res += pw
            pw *= 2
        return res