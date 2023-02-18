class Solution:
    def getXORSum(self, arr1: List[int], arr2: List[int]) -> int:
        ctr = [0] * 32
        for el in arr2:
            for b in range(32):
                if el & (1 << b):
                    ctr[b] += 1
        res = 0
        for el in arr1:
            curr = 0
            for b in range(32):
                if el & (1 << b) and ctr[b] & 1:
                    curr |= 1 << b
            res ^= curr
        return res