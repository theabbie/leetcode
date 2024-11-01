from sortedcontainers import SortedList

class Solution:
    def bestRotation(self, nums: List[int]) -> int:
        n = len(nums)
        res = (0, float('inf'))
        vals = SortedList()
        for i in range(2 * n):
            vals.add(i - nums[i % n])
            if i >= n:
                vals.remove(i - n - nums[(i - n) % n])
            if i >= n - 1:
                res = max(res, (len(vals) - vals.bisect_left(i - n + 1), n - i - 1))
        return -res[1]