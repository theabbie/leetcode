import bisect

class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        p = [0] * (n + 1)
        for i in range(n):
            p[i + 1] += p[i] + nums[i]
        res = []
        for q in queries:
            i = bisect.bisect_left(nums, q)
            res.append(i * q - p[i] + (p[-1] - p[i]) - (n - i) * q)
        return res