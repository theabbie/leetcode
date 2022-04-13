class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        mdiff = float('-inf')
        minSoFar = nums[0]
        for num in nums:
            minSoFar = min(minSoFar, num)
            mdiff = max(mdiff, num - minSoFar)
        if mdiff > 0:
            return mdiff
        return -1