class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        intervals.sort()
        prev = float('-inf')
        ctr = 0
        for a, b in intervals:
            prev = min(prev, b)
            if prev <= a:
                ctr += 1
                prev = b
        return n - ctr