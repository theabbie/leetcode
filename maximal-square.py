class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        biggest = 0
        numOnes = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "0":
                    continue
                for w in range(max(1, biggest), min(m - i, n - j) + 1):
                    curr = 0
                    valid = True
                    for p in range(w):
                        for q in range(w):
                            if matrix[i + p][j + q] != "1":
                                valid = False
                        if not valid:
                            break
                    if valid:
                        biggest = max(biggest, w)
                    else:
                        break
        return biggest * biggest