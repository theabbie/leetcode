class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        res = n * (n - 1) // 2
        ctr = {}
        for i in range(n):
            val = i - nums[i]
            res -= ctr.get(val, 0)
            ctr[val] = ctr.get(val, 0) + 1
        return res