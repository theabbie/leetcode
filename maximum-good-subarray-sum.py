from collections import defaultdict

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        firstpref = defaultdict(lambda: float('inf'))
        p = 0
        res = float('-inf')
        for i in range(n):
            firstpref[nums[i]] = min(firstpref[nums[i]], p)
            p += nums[i]
            res = max(res, p - firstpref[nums[i] - k], p - firstpref[nums[i] + k])
        if res == float('-inf'):
            return 0
        return res