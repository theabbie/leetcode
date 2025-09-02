class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        nums = [el % 2 for el in nums]
        nums.sort()
        return nums