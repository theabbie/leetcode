class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0 for i in range(n)] for j in range(n)]
        m = n
        p = 1
        k = 2 * min(m, n)
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        x, y = 0, -1
        for d in range(k):
            for i in range(n):
                x += dx[d % 4]
                y += dy[d % 4]
                res[x][y] = p
                p += 1
            m, n = n, m - 1
        return res