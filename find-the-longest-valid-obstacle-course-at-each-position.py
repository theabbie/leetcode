import bisect

class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        res = []
        b = []
        for i, el in enumerate(obstacles):
            x = bisect.bisect_left(b, (el, i))
            if x < len(b):
                b[x] = (el, i)
            else:
                b.append((el, i))
            res.append(x + 1)
        return res