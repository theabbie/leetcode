class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        for b in range(32):
            x = 0
            for el in nums:
                if el & (1 << b):
                    x += 1
            res += x * (n - x)
        return res