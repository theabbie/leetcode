class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        mx = 0
        ctr = 0
        for a, b in rectangles:
            curr = min(a, b)
            if curr == mx:
                ctr += 1
            elif curr > mx:
                ctr = 1
                mx = curr
        return ctr