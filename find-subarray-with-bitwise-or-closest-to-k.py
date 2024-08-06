class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        res = float('inf')
        last = [-1] * 32
        for i, el in enumerate(nums):
            for b in range(32):
                if not el & (1 << b):
                    last[b] = i
            ands = el
            res = min(res, abs(k - ands))
            for i in sorted(last, reverse = True):
                if i >= 0:
                    ands &= nums[i]
                    res = min(res, abs(k - ands))
        return res