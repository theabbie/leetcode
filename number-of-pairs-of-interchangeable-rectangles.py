from collections import Counter

class Solution:
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a
    
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        res = 0
        ctr = Counter()
        for l, r in rectangles:
            mul = self.gcd(l, r)
            curr = (l // mul, r // mul)
            res += ctr[curr]
            ctr[curr] += 1
        return res