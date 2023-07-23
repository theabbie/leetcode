class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        for i in range(n):
            if n % (i + 1) == 0:
                res += nums[i] * nums[i]
        return res