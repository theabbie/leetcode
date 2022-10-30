from collections import Counter

class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        ctr = Counter()
        a = []
        b = []
        for i in range(n):
            for j in range(n):
                if img1[i][j] == 1:
                    a.append((i, j))
                if img2[i][j] == 1:
                    b.append((i, j))
        for x0, y0 in a:
            for x1, y1 in b:
                ctr[(x1 - x0, y1 - y0)] += 1
        if len(ctr) == 0:
            return 0
        return max(ctr.values())