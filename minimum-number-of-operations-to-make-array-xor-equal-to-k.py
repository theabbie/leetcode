class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        for el in nums:
            k ^= el
        return k.bit_count()