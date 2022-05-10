class Solution:
    def partition(self, nums, x, beg, end):
        i = beg
        for j in range(beg, end):
            if nums[j] <= x:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        return i
    
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)
        i = self.partition(nums, 1, 0, n)
        self.partition(nums, 0, 0, i)
        return nums