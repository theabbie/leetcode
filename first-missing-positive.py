class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = set(nums)
        mnum = max(nums) + 2
        for i in range(1, mnum):
            if i not in nums:
                return i
        return 1