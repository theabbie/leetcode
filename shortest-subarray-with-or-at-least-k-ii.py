class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        if k == 0:
            return 1
        n = len(nums)
        last = [n] * 32
        res = n + 1
        for i in range(n - 1, -1, -1):
            for b in range(32):
                if nums[i] & (1 << b):
                    last[b] = i
            v = 0
            for x in sorted(last):
                if x == n:
                    break
                v |= nums[x]
                if v >= k:
                    res = min(res, x - i + 1)
        if res == n + 1:
            res = -1
        return res