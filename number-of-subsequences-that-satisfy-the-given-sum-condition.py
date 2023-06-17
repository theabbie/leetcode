import bisect

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        M = 10 ** 9 + 7
        n = len(nums)
        nums.sort()
        res = 0
        pw = [1] * (n + 1)
        for i in range(1, n + 1):
            pw[i] = 2 * pw[i - 1]
            pw[i] %= M
        for i in range(n):
            j = bisect.bisect_right(nums, target - nums[i])
            if j > i:
                res += pw[j - i - 1]
                res %= M
        return res