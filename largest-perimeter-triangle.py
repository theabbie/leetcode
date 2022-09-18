class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        i = n - 3
        while i >= 0:
            if nums[i + 2] < nums[i] + nums[i + 1]:
                return nums[i] + nums[i + 1] + nums[i + 2]
            i -= 1
        return 0