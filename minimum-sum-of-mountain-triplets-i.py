class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        res = float('inf')
        pmin = [float('inf')] * (n + 1)
        smin = [float('inf')] * (n + 1)
        for i in range(n):
            pmin[i + 1] = pmin[i]
            smin[i + 1] = smin[i]
            pmin[i + 1] = min(pmin[i + 1], nums[i])
            smin[i + 1] = min(smin[i + 1], nums[n - i - 1])
        for j in range(n):
            l = pmin[j]
            r = smin[n - j - 1]
            if l < nums[j] and r < nums[j]:
                res = min(res, l + nums[j] + r)
        if res == float('inf'):
            return -1
        return res