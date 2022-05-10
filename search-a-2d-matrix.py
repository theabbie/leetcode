class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        beg = 0
        end = m * n - 1
        while beg <= end:
            mid = (beg + end) // 2
            i = mid // n
            j = mid % n
            if matrix[i][j] == target:
                return True
            elif beg == end:
                break
            elif matrix[i][j] < target:
                beg = mid + 1
            else:
                end = mid
        return False