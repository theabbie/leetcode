class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = 0
        for i in range(n):
            good = True
            if i - k >= 0 and nums[i - k] >= nums[i]:
                good = False
            if i + k < n and nums[i + k] >= nums[i]:
                good = False
            if good:
                res += nums[i]
        return res