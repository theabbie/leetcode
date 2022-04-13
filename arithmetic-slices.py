class Solution:
    def numSlicesEndingHere(self, nums, i, n):
        if i < 2:
            return 0
        if i == 2:
            if nums[2] - nums[1] == nums[1] - nums[0]:
                return 1
            return 0
        if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
            return 1 + self.numSlicesEndingHere(nums, i - 1, n)
        return 0
    
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        ctr = 0
        for i in range(n):
            ctr += self.numSlicesEndingHere(nums, i, n)
        return ctr