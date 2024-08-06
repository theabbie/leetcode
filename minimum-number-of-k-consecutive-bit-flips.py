class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n = len(nums)
        diffs = [0] * (n + 1)
        res = 0
        for i in range(n):
            if i > 0:
                diffs[i] += diffs[i - 1]
            if diffs[i] & 1:
                nums[i] = 1 - nums[i]
            if i + k <= n and nums[i] == 0:
                res += 1
                nums[i] = 1
                diffs[i] += 1
                diffs[i + k] -= 1
        if sum(nums) != n:
            return -1
        return res