class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        bi = "{:b}".format(n)
        for i, c in enumerate(bi):
            if i > 0:
                if c == bi[i - 1]:
                    return False
        return True