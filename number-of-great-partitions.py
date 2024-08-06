class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        M = 10 ** 9 + 7
        s = sum(nums)
        if k >= s - k:
            return 0
        fc = {}
        def countf(i, s):
            if s >= k:
                return 0
            if i >= len(nums):
                return 1
            if (i, s) in fc:
                return fc[(i, s)]
            res = countf(i + 1, s + nums[i]) + countf(i + 1, s)
            res %= M
            fc[(i, s)] = res
            return res
        res = 2 * countf(0, 0)
        res = pow(2, len(nums), M) - res
        res %= M
        return res