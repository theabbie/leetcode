class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m = len(mat)
        n = len(mat[0])
        p = [[0] * (n + 1) for _ in range(m)]
        for i in range(m):
            for j in range(n):
                p[i][j + 1] += p[i][j] + mat[i][j]
        beg = 1
        end = min(m, n)
        res = 0
        while beg <= end:
            mid = (beg + end) // 2
            found = False
            for i in range(m - mid + 1):
                for j in range(n - mid + 1):
                    s = 0
                    for k in range(i, i + mid):
                        s += p[k][j + mid] - p[k][j]
                    if s <= threshold:
                        found = True
                        break
            if found:
                res = mid
                beg = mid + 1
            else:
                end = mid - 1
        return res