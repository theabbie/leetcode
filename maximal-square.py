class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        biggest = 0
        for i in range(m):
            for j in range(n):
                for w in range(biggest, min(m - i, n - j) + 1):
                    valid = True
                    for p in range(w):
                        for q in range(w):
                            if matrix[i + p][j + q] != "1":
                                valid = False
                                break
                        if not valid:
                            break
                    if valid:
                        biggest = max(biggest, w)
                    else:
                        break
        return biggest * biggest