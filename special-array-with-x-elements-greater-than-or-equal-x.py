class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        i = 0
        while i < len(nums) and nums[i] > i:
            i += 1
        if i < len(nums) and i == nums[i]:
            return -1
        return i