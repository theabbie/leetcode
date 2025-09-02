class Solution:
    def maxSum(self, nums: List[int]) -> int:
        if max(nums) < 0:
            return max(nums)
        return sum(el for el in set(nums) if el >= 0)