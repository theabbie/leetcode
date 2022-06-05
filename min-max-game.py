class Solution:
    def minMax(self, nums, i, j, minm):
        if j == i + 1:
            return nums[i]
        mid = (i + j) // 2
        a = self.minMax(nums, i, mid, True)
        b = self.minMax(nums, mid, j, False)
        if minm:
            return min(a, b)
        return max(a, b)
    
    def minMaxGame(self, nums: List[int]) -> int:
        n = len(nums)
        return self.minMax(nums, 0, n, True)