class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        vals = [(el, 0) for el in horizontalCut] + [(el, 1) for el in verticalCut]
        vals.sort()
        res = 0
        r = m
        c = n
        for x, t in vals:
            if t == 0:
                res += c * x
                r -= 1
            else:
                res += r * x
                c -= 1
        return res