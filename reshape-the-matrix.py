class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        if m * n != r * c:
            return mat
        for i in range(0, r * c, c):
            mat.append([])
            for j in range(i, i + c):
                mat[-1].append(mat[j // n][j % n])
        return mat[m:]