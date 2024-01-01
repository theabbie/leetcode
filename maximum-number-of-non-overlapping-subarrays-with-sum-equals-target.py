class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        n = len(nums)
        pos = {}
        p = 0
        pos[p] = 0
        prev = -1
        res = 0
        for i in range(n):
            p += nums[i]
            if pos.get(p - target, -1) > prev:
                res += 1
                prev = i
            pos[p] = i + 1
        return res