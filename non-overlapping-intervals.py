class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])
        prev = float('-inf')
        res = len(intervals)
        for a, b in intervals:
            if a >= prev:
                res -= 1
                prev = b
        return res