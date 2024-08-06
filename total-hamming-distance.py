class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        res = 0
        ctr = [0] * 32
        for i, el in enumerate(nums):
            for b in range(32):
                if el & (1 << b):
                    res += i - ctr[b]
                    ctr[b] += 1
                else:
                    res += ctr[b]
        return res