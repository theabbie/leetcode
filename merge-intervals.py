class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        n = len(intervals)
        i = 0
        while i < len(intervals) - 1:
            if intervals[i][1] >= intervals[i + 1][0]:
                if intervals[i][1] <= intervals[i + 1][1]:
                    intervals[i][1] = intervals[i + 1][1]
                intervals.pop(i + 1)
            else:
                i += 1
        return intervals