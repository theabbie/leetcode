class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        k %= len(mat[0])
        for i in range(len(mat)):
            curr = mat[i][:]
            curr[:k] = curr[:k][::-1]
            curr[k:] = curr[k:][::-1]
            curr[:] = curr[::-1]
            if curr != mat[i]:
                return False
            k = len(mat[0]) - k
        return True