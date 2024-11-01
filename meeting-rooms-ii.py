class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        v = []
        for a, b in intervals:
            v.append((a, 1))
            v.append((b, -1))
        v.sort()
        res = 0
        p = 0
        for x, d in v:
            p += d
            res = max(res, p)
        return res