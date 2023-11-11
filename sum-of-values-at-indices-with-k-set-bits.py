class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = 0
        for i in range(n):
            if i.bit_count() == k:
                res += nums[i]
        return res