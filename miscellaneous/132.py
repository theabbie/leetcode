class Solution:
    def find132pattern(self, nums):
        currMin = float('inf')
        currMax = float('-inf')
        for num in nums:
            currMin = min(currMin, num)
            currMax = max(currMax, num)
            if num > currMin and num < currMax:
                return True
            print(currMin, currMax)
        return False

print(Solution().find132pattern([3, 1, 4, 2]))