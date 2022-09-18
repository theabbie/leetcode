class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        pr = [0 for _ in range(m)]
        pc = [0 for _ in range(n)]
        for i in range(m):
            for j in range(n):
                pr[i] += mat[i][j]
                pc[j] += mat[i][j]
        res = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1 and pr[i] == 1 and pc[j] == 1:
                    res += 1
        return res