class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        pref = [float('-inf')] * (n + 1)
        for i in range(n):
            pref[i + 1] = max(pref[i], nums[i])
        msuff = float('-inf')
        for i in range(n - 1, -1, -1):
            if i < n - 1:
                res = max(res, msuff * (pref[i] - nums[i]))
            msuff = max(msuff, nums[i])
        return res