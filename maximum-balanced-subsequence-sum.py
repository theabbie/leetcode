import numpy as np

class Solution:
    def maxBalancedSubsequenceSum(self, nums: List[int]) -> int:
        n = len(nums)
        mp = {}
        for i in range(n):
            mp[nums[i] - i] = 0
        for i, el in enumerate(sorted(mp)):
            mp[el] = i
        fw = np.array([float('-inf')] * (len(mp) + 1))
        res = float('-inf')
        for i in range(n):
            curr = nums[i] + np.max(fw[:mp[nums[i] - i] + 1])
            curr = max(curr, nums[i])
            fw[mp[nums[i] - i]] = curr
            res = max(res, curr)
        return int(res)