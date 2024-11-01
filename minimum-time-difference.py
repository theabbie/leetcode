class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def minutes(a):
            h = int(a.split(":")[0])
            m = int(a.split(":")[1])
            return 60 * h + m
        timePoints.sort()
        timePoints.append(timePoints[0])
        res = float('inf')
        for i in range(len(timePoints) - 1):
            a = minutes(timePoints[i])
            b = minutes(timePoints[i+1])
            diff = abs(a - b)
            diff = min(diff, 24 * 60 - diff)
            res = min(res, diff)
        return res