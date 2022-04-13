class Solution:
    def isIncreasing(self, nums, n):
        for i in range(n - 1):
            if nums[i + 1] <= nums[i]:
                return False
        return True
    
    def canBeIncreasing(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(n):
            if self.isIncreasing(nums[: i] + nums[i + 1 :], n - 1):
                return True
        return False