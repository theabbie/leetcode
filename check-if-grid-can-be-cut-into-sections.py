class Solution:
    def merge(self, intervals):
        res = []
        intervals.sort()
        prev = float('-inf')
        for l, r in intervals:
            if l < prev:
                res[-1][-1] = max(res[-1][1], r)
            else:
                res.append([l, r])
            prev = res[-1][1]
        return res
    
    def check(self, intervals):
        intervals = self.merge(intervals)
        return len(intervals) >= 3
    
    def checkValidCuts(self, n: int, rectangles):
        a = [[x0, x1] for x0, y0, x1, y1 in rectangles]
        b = [[y0, y1] for x0, y0, x1, y1 in rectangles]
        return self.check(a) or self.check(b)