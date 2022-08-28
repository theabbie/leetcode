from sortedcontainers import SortedList

class Solution:
    def maxSub(self, arr, m, k):
        msum = float('-inf')
        bst = SortedList()
        bst.add(0)
        c = 0
        for i in range(m):
            c += arr(i)
            prev = bst.bisect_left(c - k)
            if prev < len(bst):
                msum = max(msum, c - bst[prev])
            bst.add(c)
        return msum
    
    def maxSumSubmatrix(self, matrix, k):
        m = len(matrix)
        n = len(matrix[0])
        res = float('-inf')
        p = [[0] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                p[i].append(p[i][-1] + matrix[i][j])
        for i in range(n + 1):
            for j in range(n - 1, i - 1, -1):
                arr = lambda x: p[x][j + 1] - p[x][i]
                res = max(res, self.maxSub(arr, m, k))
                if res == k:
                    break
        return res