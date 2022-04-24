from collections import defaultdict
import bisect

class Solution:
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        n = len(rectangles)
        heights = defaultdict(list)
        for l, h in rectangles:
            bisect.insort(heights[h], l)
        count = []
        for x, y in points:
            ctr = 0
            for h in range(y, 101):
                ctr += len(heights[h]) - bisect.bisect_left(heights[h], x)
            count.append(ctr)
        return count