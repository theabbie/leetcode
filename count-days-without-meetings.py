class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        intervals.sort()
        prev = float('-inf')
        res = []
        for a, b in intervals:
            if a > prev:
                res.append([a, b])
            else:
                res[-1][1] = max(res[-1][1], b)
            prev = max(prev, b)
        return res
    
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings = self.merge(meetings)
        res = days
        for x, y in meetings:
            res -= y - x + 1
        return res