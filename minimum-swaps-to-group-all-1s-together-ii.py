class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        p = [0]
        k = 0
        for el in nums:
            p.append(p[-1] + el)
            if el == 1:
                k += 1
        res = float('inf')
        for i in range(n):
            if i <= n - k:
                res = min(res, k - p[i + k] + p[i])
            if i <= k:
                res = min(res, p[i + n - k] - p[i])
        return res