import numpy as np

class Solution:
    def countVowelStrings(self, n):
        mat = np.array(
            [
                [1, 0, 0, 0, 0],
                [1, 1, 0, 0, 0],
                [1, 1, 1, 0, 0],
                [1, 1, 1, 1, 0],
                [1, 1, 1, 1, 1],
            ]
        )
        seed = np.array([1, 0, 0, 0, 0])
        res = np.linalg.matrix_power(mat, n).dot(seed)
        return np.sum(res)