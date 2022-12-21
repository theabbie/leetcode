from collections import defaultdict

class Solution:
    def dist(self, a, b):
        return (b[0] - a[0]) * (b[0] - a[0]) + (b[1] - a[1]) * (b[1] - a[1])

    def area(self, a, b, c, d):
        if self.dist(a, c) != self.dist(b, d):
            return float('inf')
        if a[0] + c[0] != b[0] + d[0] or a[1] + c[1] != b[1] + d[1]:
            return float('inf')
        return self.dist(a, b) * self.dist(a, d)
    
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a
    
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        n = len(points)
        pairs = defaultdict(lambda: defaultdict(list))
        for i in range(n):
            for j in range(i + 1, n):
                a, b = points[i]
                c, d = points[j]
                x, y = c - a, d - b
                if y < 0:
                    x, y = -x, -y
                mul = self.gcd(abs(x), abs(y))
                x //= mul
                y //= mul
                if x >= 0 and y >= 0:
                    pairs[(x, y)][self.dist((a, b), (c, d))].append((i, j))
        res = float('inf')
        for slope in pairs:
            for d in pairs[slope]:
                m = len(pairs[slope][d])
                for i in range(m):
                    for j in range(i + 1, m):
                        p, q = pairs[slope][d][i]
                        r, s = pairs[slope][d][j]
                        p, q, s, r = sorted([p, q, r, s], key = lambda x: points[x])
                        res = min(res, self.area(points[p], points[q], points[r], points[s]))
        if res == float('inf'):
            return 0
        return res ** 0.5