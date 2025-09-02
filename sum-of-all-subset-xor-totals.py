class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        return (1 << len(nums) - 1) * reduce(lambda x, y: x | y, nums)