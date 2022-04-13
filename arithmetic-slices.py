class Solution:
    def numSlicesEndingHere(self, nums, i, n):
        if i in self.cache:
            return self.cache[i]
        if i < 2:
            return 0
        if i == 2:
            if nums[2] - nums[1] == nums[1] - nums[0]:
                self.cache[i] = 1
                return 1
            self.cache[i] = 0
            return 0
        if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
            val = 1 + self.numSlicesEndingHere(nums, i - 1, n)
            self.cache[i] = val
            return val
        self.cache[i] = 0
        return 0
    
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        self.cache = {}
        ctr = 0
        for i in range(n):
            ctr += self.numSlicesEndingHere(nums, i, n)
        return ctr