class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        if m * n != r * c:
            return mat
        mat = [i for j in mat for i in j]
        for i in range(r):
            mat.extend([mat[i * c : (i + 1) * c]])
        return mat[m * n :]