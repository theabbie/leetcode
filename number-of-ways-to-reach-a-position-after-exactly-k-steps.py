class Solution:
    def perm(self, n, k):
        C = [[0 for x in range(k+1)] for x in range(n+1)]
        for i in range(n+1):
            for j in range(min(i, k)+1):
                if j == 0 or j == i:
                    C[i][j] = 1
                else:
                    C[i][j] = C[i-1][j-1] + C[i-1][j]
        return C[n][k]
    
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        diff = endPos - startPos
        if (diff + k) % 2 != 0:
            return 0
        x = (diff + k) // 2
        return self.perm(k, x) % (10 ** 9 + 7)