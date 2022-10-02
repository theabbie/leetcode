class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        maxTillNow = float('-inf')
        minTillNow = float('inf')
        maxSoFar = float('-inf')
        minSoFar = float('inf')
        total = 0
        for el in nums:
            total += el
            maxTillNow = max(el, el + maxTillNow)
            minTillNow = min(el, el + minTillNow)
            maxSoFar = max(maxSoFar, maxTillNow)
            minSoFar = min(minSoFar, minTillNow)
        if minSoFar == total:
            return maxSoFar
        return max(maxSoFar, total - minSoFar)