class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        n = len(nums)
        minvals = [0] * n
        minvals[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            minvals[i] = min(nums[i], minvals[i + 1])
        currmax = float('-inf')
        for i in range(n - 1):
            currmax = max(currmax, nums[i])
            if currmax <= minvals[i + 1]:
                return i + 1