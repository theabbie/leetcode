class Solution:
    def merge(self, intervals):
        res = []
        intervals.sort()
        prev = float('-inf')
        for l, r in intervals:
            if l <= prev:
                res[-1][-1] = max(res[-1][1], r)
            else:
                res.append([l, r])
            prev = res[-1][1]
        return res
    
    def countDays(self, days, meetings):
        meetings = self.merge(meetings)
        return days - sum(r - l + 1 for l, r in meetings)