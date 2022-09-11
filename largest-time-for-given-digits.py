from itertools import permutations

class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        p = permutations(arr)
        maxtime = (float('-inf'), float('-inf'))
        for t in p:
            h = 10 * t[0] + t[1]
            m = 10 * t[2] + t[3]
            if 0 <= h < 24 and 0 <= m < 60:
                maxtime = max(maxtime, (h, m))
        if maxtime == (float('-inf'), float('-inf')):
            return ""
        return f"{maxtime[0]:02d}:{maxtime[1]:02d}"