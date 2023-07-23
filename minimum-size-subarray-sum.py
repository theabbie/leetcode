class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        s = 0
        res = n + 1
        for j in range(n):
            s += nums[j]
            while i < j and s - nums[i] >= target:
                s -= nums[i]
                i += 1
            if s >= target:
                res = min(res, j - i + 1)
        if res == n + 1:
            return 0
        return res