class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        mx = nums[:]
        mn = nums[:]
        for i in range(n - 2, -1, -1):
            mx[i] = max(mx[i], mx[i + 1])
            mn[i] = min(mn[i], mn[i + 1])
        res = 0
        mnval = float('inf')
        mxval = float('-inf')
        for j in range(n - 1):
            for l in [mnval, mxval]:
                for r in [mn[j + 1], mx[j + 1]]:
                    if j > 0:
                        res = max(res, (l - nums[j]) * r)
            mnval = min(mnval, nums[j])
            mxval = max(mxval, nums[j])
        return res