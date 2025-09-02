class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        res = [1,2,4]
        p = 8
        while len(res) < n:
            res.extend([p] * (p // 2))
            p *= 2
        return res[n - 1]