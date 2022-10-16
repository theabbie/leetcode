class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        exists = set(nums)
        return max([num for num in nums if -num in exists] + [-1])