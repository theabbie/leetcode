class Solution:
    def concatenatedBinary(self, n: int) -> int:
        MAX = 10 ** 9 + 7
        res = 0
        for i in range(1, n + 1):
            k = len("{:b}".format(i))
            res = (res << k) | i
            res %= MAX
        return res