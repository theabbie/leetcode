import bisect

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            j = bisect.bisect_left(matrix[i], target)
            j = min(j, n - 1)
            if matrix[i][j] == target:
                return True
        return False