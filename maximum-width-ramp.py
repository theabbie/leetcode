class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        n = len(nums)
        vals = [(nums[i], i) for i in range(n)]
        vals.sort()
        minval = float('inf')
        res = 0
        for v, i in vals:
            res = max(res, i - minval)
            minval = min(minval, i)
        return res