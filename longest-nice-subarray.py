class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        for i in range(n):
            OR = 0
            j = i
            while j < n:
                if OR & nums[j] > 0:
                    break
                OR |= nums[j]
                j += 1
            res = max(res, j - i)
        return res