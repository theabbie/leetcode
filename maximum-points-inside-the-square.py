from collections import defaultdict

class Solution:
    def maxPointsInsideSquare(self, points: List[List[int]], s: str) -> int:
        n = len(points)
        vals = defaultdict(list)
        for i in range(n):
            vals[max(abs(points[i][0]), abs(points[i][1]))].append(s[i])
        res = 0
        gb = set()
        for l in sorted(vals):
            curr = set()
            currctr = 0
            valid = True
            for c in vals[l]:
                if c in curr or c in gb:
                    valid = False
                    break
                curr.add(c)
                currctr += 1
            if not valid:
                break
            gb.update(curr)
            res += currctr
        return res