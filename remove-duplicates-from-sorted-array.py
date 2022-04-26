class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        for j in range(n):
            if j > 0 and nums[j] != nums[j - 1]:
                i += 1
                nums[i] = nums[j]
        return i + 1