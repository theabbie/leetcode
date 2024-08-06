from sortedcontainers import SortedList
from collections import *

class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        n = len(points)
        points.sort()
        yvals = defaultdict(list)
        res = 0
        for x, y in points:
            yvals[x].append(y)
        xes = sorted(yvals)
        for i in range(len(xes)):
            res += len(yvals[xes[i]]) - 1
            bst = SortedList(yvals[xes[i]])
            for j in range(i + 1, len(xes)):
                for y in yvals[xes[j]]:
                    bst.add(y)
                for ly in yvals[xes[i]]:
                    for ry in yvals[xes[j]]:
                        if ly >= ry and bst.bisect_right(ly) - bst.bisect_left(ry) == 2:
                            res += 1
        return res