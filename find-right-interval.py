import bisect

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        ans = [-1 for i in range(n)]
        starts = []
        ends = []
        for k in range(n):
            i, j = intervals[k]
            bisect.insort(starts, (i, k))
            bisect.insort(ends, (j, k))
        sinx = [s[0] for s in starts]
        lst = len(starts)
        for end, i in ends:
            pos = bisect.bisect_left(sinx, end)
            if pos < lst:
                ans[i] = starts[pos][1]
        return ans