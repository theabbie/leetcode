class Solution:
    def isPossible(self, heights, i, j, m, n, visited, k):
        if (i, j) == (m - 1, n - 1):
            return True
        for (x, y) in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
            if 0 <= x < m and 0 <= y < n and (x, y) not in visited:
                effort = abs(heights[x][y] - heights[i][j])
                if effort <= k:
                    visited.add((x, y))
                    if self.isPossible(heights, x, y, m, n, visited, k):
                        return True
        return False
    
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m = len(heights)
        n = len(heights[0])
        beg = 0
        end = 1
        while not self.isPossible(heights, 0, 0, m, n, {(0, 0)}, end):
            end = end << 1
        while beg <= end:
            mid = (beg + end) // 2
            iscurrpossible = self.isPossible(heights, 0, 0, m, n, {(0, 0)}, mid)
            isprevpossible = self.isPossible(heights, 0, 0, m, n, {(0, 0)}, mid - 1)
            if not isprevpossible and iscurrpossible:
                return mid
            elif beg == end:
                break
            elif not isprevpossible and not iscurrpossible:
                beg = mid + 1
            elif isprevpossible and iscurrpossible:
                end = mid
        return beg