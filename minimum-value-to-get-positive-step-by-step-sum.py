class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        curr = 0
        minval = float('inf')
        for el in nums:
            curr += el
            minval = min(minval, curr)
        return max(1 - minval, 1)