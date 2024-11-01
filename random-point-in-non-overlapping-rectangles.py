from random import *
import bisect

class Solution:
    def __init__(self, rects: List[List[int]]):
        p = [0]
        for a, b, x, y in rects:
            p.append(p[-1] + (x - a + 1) * (y - b + 1))
        self.p = p
        self.rects = rects

    def pick(self):
        i = bisect.bisect_left(self.p, randint(0, self.p[-1]))
        a, b, x, y = self.rects[i - 1]
        return [randint(a, x), randint(b, y)]