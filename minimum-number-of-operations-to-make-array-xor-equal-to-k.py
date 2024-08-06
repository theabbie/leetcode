class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        val = 0
        for el in nums:
            for b in range(32):
                if el & (1 << b):
                    val ^= (1 << b)
        return "{:0b}".format(val ^ k).count("1")