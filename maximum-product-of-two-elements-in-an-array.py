class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        a, b = 0, 0
        for el in nums:
            temp, a, b = sorted([a, b, el])
        return (a - 1) * (b - 1)