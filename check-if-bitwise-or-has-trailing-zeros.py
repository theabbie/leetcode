class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        even = 0
        for el in nums:
            if el % 2 == 0:
                even += 1
        return even >= 2