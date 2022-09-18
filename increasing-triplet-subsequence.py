class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        biggest = [float('-inf')] * (n + 1)
        for i in range(n - 1, -1, -1):
            biggest[i] = max(nums[i], biggest[i + 1])
        minyet = float('inf')
        for i in range(n):
            if minyet < nums[i] < biggest[i + 1]:
                return True
            minyet = min(minyet, nums[i])
        return False