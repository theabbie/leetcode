class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        maxsum = 0
        minyet = float('inf')
        maxyet = float('-inf')
        for el in nums:
            minyet = min(el, minyet + el)
            maxyet = max(el, maxyet + el)
            maxsum = max(maxsum, maxyet, -minyet)
        return maxsum