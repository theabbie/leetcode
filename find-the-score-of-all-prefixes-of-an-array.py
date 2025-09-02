class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        m = 0
        for i in range(len(nums)):
            m = max(m, nums[i])
            nums[i] += m
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        return nums