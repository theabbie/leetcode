class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pk = [0] * (n + 1)
        for i in range(n):
            pk[i + 1] = pk[i] + int(nums[i] == k)
        res = 0
        p = [0] * (n + 1)
        for v in set(nums):
            for i in range(n):
                p[i + 1] = p[i] + int(nums[i] == v)
            mn = float('inf')
            for j in range(n):
                mn = min(mn, p[j] - pk[j])
                res = max(res, pk[n] - pk[j + 1] + p[j + 1] - mn)
        return res