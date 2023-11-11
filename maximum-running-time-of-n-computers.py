class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        beg = 0
        end = sum(batteries)
        res = beg
        while beg <= end:
            mid = (beg + end) // 2
            used = 0
            for el in batteries:
                used += min(el, mid)
            if used >= mid * n:
                res = mid
                beg = mid + 1
            else:
                end = mid - 1
        return res