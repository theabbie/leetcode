class Solution:
    def rectangleArea(self, rectangles):
        res = 0
        for x0, y0, x1, y1 in rectangles:
            res += (x1 - x0) * (y1 - y0)
        return res
    
    def split(self, squares, y):
        below = []
        above = []
        for x, yi, li in squares:
            if yi + li <= y:
                below.append((x, yi, x + li, yi + li))
            elif yi >= y:
                above.append((x, yi, x + li, yi + li))
            else:
                below.append((x, yi, x + li, y))
                above.append((x, y, x + li, yi + li))
        return below, above
    
    def separateSquares(self, squares: List[List[int]]) -> float:
        def check(y):
            b, a = self.split(squares, y)
            return self.rectangleArea(b) >= self.rectangleArea(a)
        end = 1
        while not check(end):
            end *= 2
        beg = end / 2
        while end - beg > 1e-6:
            mid = (beg + end) / 2
            if check(mid):
                end = mid
            else:
                beg = mid
        return end