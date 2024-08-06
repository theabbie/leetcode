class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        maxsum = float('-inf')
        minsum = float('inf')
        res = 0
        for el in nums:
            maxsum = max(el, el + maxsum)
            minsum = min(el, el + minsum)
            res = max(res, abs(minsum), abs(maxsum))
        return res