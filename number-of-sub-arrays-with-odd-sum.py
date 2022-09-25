class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        z = 1
        o = 0
        p = 0
        res = 0
        for el in arr:
            p = (p + el) % 2
            if p == 0:
                res += o
                z += 1
            else:
                res += z
                o += 1
        return res % (10 ** 9 + 7)