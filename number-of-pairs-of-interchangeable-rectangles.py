def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        res = 0
        ctr = {}
        for w, h in rectangles:
            mul = gcd(w, h)
            w //= mul
            h //= mul
            res += ctr.get((w, h), 0)
            ctr[(w, h)] = ctr.get((w, h), 0) + 1
        return res