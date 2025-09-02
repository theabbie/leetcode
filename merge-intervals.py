class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
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