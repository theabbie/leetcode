class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return
        curr = nums[0]
        i = 1
        while i < len(nums):
            if nums[i] == curr:
                nums.pop(i)
                i -= 1
            curr = nums[i]
            i += 1