class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        ctr = {}
        for a, b in rectangles:
            ctr[min(a, b)] = ctr.get(min(a, b), 0) + 1
        return ctr[max(ctr.keys())]