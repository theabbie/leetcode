class Solution:
    def findMaximumScore(self, nums: List[int]) -> int:
        n = len(nums)
        prev = 0
        res = 0
        for i in range(n):
            if i == n - 1 or nums[i] > nums[prev]:
                res += (i - prev) * nums[prev]
                prev = i
        return res