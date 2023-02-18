class Solution:
    def xorBeauty(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        ctr = [0] * 32
        for el in nums:
            for b in range(32):
                if el & (1 << b):
                    ctr[b] += 1
        for el in nums:
            curr = 0
            for b in range(32):
                sets = 0
                unsets = 0
                if el & (1 << b):
                    sets += ctr[b]
                    unsets += n - ctr[b]
                else:
                    unsets += n
                if sets & 1:
                    curr |= 1 << b
            res ^= curr
        return res