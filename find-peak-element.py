class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            left = nums[i] > nums[i - 1] if i > 0 else True
            right = nums[i] > nums[i + 1] if i < n - 1 else True
            if left and right:
                return i