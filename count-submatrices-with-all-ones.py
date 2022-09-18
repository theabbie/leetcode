class Solution:
    def numsubs(self, arr, k, n):
        res = 0
        i = 0
        while i < n:
            ctr = 1
            while i < n - 1 and arr(i) == arr(i + 1):
                i += 1
                ctr += 1
            i += 1
            if arr(i - 1) == k:
                res += ctr * (ctr + 1) // 2
        return res
    
    def numSubmat(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        p = [[0] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                p[i].append(p[i][-1] + mat[i][j])
        res = 0
        for i in range(n):
            for j in range(i + 1, n + 1):
                arr = lambda x: p[x][j] - p[x][i]
                res += self.numsubs(arr, j - i, m)
        return res