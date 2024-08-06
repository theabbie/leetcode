class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0
        for b in range(32):
            o = z = 0
            for el in nums:
                if el & (1 << b):
                    o += 1
                else:
                    z += 1
            res += pow(2, z + b) * (pow(2, o - 1) if o > 0 else 0)
        return res