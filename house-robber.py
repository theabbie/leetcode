class Solution:
    def robRec(self, nums, i, n):
        if i >= n:
            return 0
        if i == n - 1:
            return nums[i]
        if i in self.cache:
            return self.cache[i]
        maxRob = nums[i]
        for j in range(i + 2, n):
            maxRob = max(maxRob, nums[i] + self.robRec(nums, j, n))
        self.cache[i] = maxRob
        return maxRob
    
    def rob(self, nums: List[int]) -> int:
        self.cache = {}
        return max(self.robRec(nums, 0, len(nums)), self.robRec(nums, 1, len(nums)))