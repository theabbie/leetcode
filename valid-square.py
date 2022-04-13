class Solution:
    def dist(self, a, b):
        return (a[0] - b[0]) * (a[0] - b[0]) + (a[1] - b[1]) * (a[1] - b[1])
    
    def isPerpendicular(self, a, b, c, d):
        return (b[1] - a[1]) * (d[1] - c[1]) == (b[0] - a[0]) * (c[0] - d[0])
    
    def midPoint(self, a, b):
        return (a[0] + b[0], a[1] + b[1])
    
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        plist = [p1, p2, p3, p4]
        points = [[(0, 1), (2, 3)], [(0, 2), (1, 3)], [(0, 3), (1, 2)]]
        for diag in points:
            a, b = [plist[d] for d in diag[0]]
            c, d = [plist[d] for d in diag[1]]
            isBisector = self.midPoint(a, b) == self.midPoint(c, d)
            if not isBisector:
                continue
            d1, d2 = self.dist(a, b), self.dist(c, d)
            if d1 != d2 or d1 == 0:
                continue
            if self.isPerpendicular(a, b, c, d):
                return True
        return False