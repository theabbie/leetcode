import bisect

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        MAX = 10 ** 9 + 7
        n = len(nums)
        nums.sort()
        res = 0
        for i in range(n):
            j = bisect.bisect_right(nums, target - nums[i])
            if j > i:
                ctr = 1 << j - i - 1
                res = (res + ctr) % MAX
        return res