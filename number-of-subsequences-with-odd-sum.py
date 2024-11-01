class Solution:
    def subsequenceCount(self, nums: List[int]) -> int:
        M = 10 ** 9 + 7
        n = len(nums)
        o = e = 0
        for el in nums:
            if el & 1:
                o += 1
            else:
                e += 1
        if o == 0:
            return 0
        return pow(2, o + e - 1, M)