class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        n = len(nums)
        beauty = 0
        minvals = [0] * n
        minvals[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            minvals[i] = min(nums[i], minvals[i + 1])
        currmax = float('-inf')
        for i in range(n):
            if 1 <= i <= n - 2:
                if currmax < nums[i] < minvals[i + 1]:
                    beauty += 2
                elif nums[i - 1] < nums[i] < nums[i + 1]:
                    beauty += 1
            currmax = max(currmax, nums[i])
        return beauty