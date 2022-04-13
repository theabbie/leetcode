class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n = nums[0]
        for num in nums[1:]:
            n = n ^ num
        return n