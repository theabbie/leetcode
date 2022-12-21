class Solution:
    def numsmaller(self, matrix, m, n, x):
        res = 0
        for i in range(m):
            beg = 0
            end = n - 1
            curr = n
            while beg <= end:
                mid = (beg + end) // 2
                if matrix[i][mid] <= x:
                    beg = mid + 1
                else:
                    curr = mid
                    end = mid - 1
            res += curr
        return res
    
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        m = len(matrix)
        n = len(matrix[0])
        beg = matrix[0][0]
        end = matrix[m - 1][n - 1]
        res = -1
        while beg <= end:
            mid = (beg + end) // 2
            curr = self.numsmaller(matrix, m, n, mid)
            if curr >= k:
                res = mid
                end = mid - 1
            else:
                beg = mid + 1
        return res