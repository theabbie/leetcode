class FenwickTree:
    def __init__(self, x):
        self.bit = x

    def update(self, idx, x):
        while idx < len(self.bit):
            self.bit[idx] = max(self.bit[idx], x)
            idx |= idx + 1

    def query(self, end):
        x = 0
        while end:
            x = max(x, self.bit[end - 1])
            end &= end - 1
        return x

class Solution:
    def maxPathLength(self, coordinates: List[List[int]], k: int) -> int:
        x = {}
        for a, b in coordinates:
            x[b] = 0
        for i, el in enumerate(sorted(x)):
            x[el] = i
        M = len(x)
        n = len(coordinates)
        for i in range(n):
            coordinates[i][1] = x[coordinates[i][1]]
            coordinates[i].append(i)
        coordinates.sort()
        groups = {}
        for x, y, pos in coordinates:
            if x not in groups:
                groups[x] = []
            groups[x].append((y, pos))
        left = 0
        right = 0
        groups = sorted(groups.items())
        fw = FenwickTree([0] * (M + 1))
        for i in range(len(groups) - 1, -1, -1):
            curr = groups[i][1]
            vals = []
            for v, pos in curr:
                l = 1 + fw.query(M - v - 1)
                if pos == k:
                    right = l
                vals.append(l)
            for j in range(len(curr)):
                fw.update(M - curr[j][0] - 1, vals[j])
        fw = FenwickTree([0] * (M + 1))
        for i in range(len(groups)):
            curr = groups[i][1]
            vals = []
            for v, pos in curr:
                l = 1 + fw.query(v)
                if pos == k:
                    left = l
                vals.append(l)
            for j in range(len(curr)):
                fw.update(curr[j][0], vals[j])
        return left + right - 1