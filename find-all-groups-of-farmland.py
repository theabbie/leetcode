class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        m = len(land)
        n = len(land[0])
        res = []
        for i in range(m):
            for j in range(n):
                if land[i][j] == 1:
                    if (i == 0 or land[i - 1][j] == 0) and (j == 0 or land[i][j - 1] == 0):
                        k, l = i, j
                        while k < m - 1 and land[k + 1][j] == 1:
                            k += 1
                        while l < n - 1 and land[i][l + 1] == 1:
                            l += 1
                        res.append([i, j, k, l])
        return res