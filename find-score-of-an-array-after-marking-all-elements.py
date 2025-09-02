from sortedcontainers import SortedList

class Solution:
    def findScore(self, nums: List[int]) -> int:
        n = len(nums)
        vals = SortedList()
        for i in range(n):
            vals.add((nums[i], i))
        res = 0
        while vals:
            v, pos = vals.pop(0)
            res += v
            for x in [pos - 1, pos + 1]:
                if 0 <= x < n and (nums[x], x) in vals:
                    vals.remove((nums[x], x))
        return res