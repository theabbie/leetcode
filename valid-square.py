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
        for d1, d2 in points:
            a, b = [plist[d] for d in d1]
            c, d = [plist[d] for d in d2]
            
            if self.dist(a, b) == self.dist(c, d) and self.dist(a, b) > 0 and self.midPoint(a, b) == self.midPoint(c, d) and self.isPerpendicular(a, b, c, d):
                return True
        return False