class Solution:
    def maximumXOR(self, nums: List[int]) -> int:
        res = 0
        for el in nums:
            res |= el
        return res