M = 10 ** 9 + 7

class FenwickTree:
    def __init__(self, x):
        self.bit = x
        for i in range(len(x)):
            j = i | (i + 1)
            if j < len(x):
                x[j] += x[i]
                x[j] %= M

    def update(self, idx, x):
        while idx < len(self.bit):
            self.bit[idx] += x
            self.bit[idx] %= M
            idx |= idx + 1

    def query(self, end):
        x = 0
        while end:
            x += self.bit[end - 1]
            x %= M
            end &= end - 1
        return x

class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        dp = [[[0, 0] for _ in range(one + 1)] for _ in range(zero + 1)]
        dp[0][0][0] = dp[0][0][1] = 1
        rowsz = []
        rowso = []
        colsz = []
        colso = []
        for i in range(zero + 1):
            rowsz.append(FenwickTree([dp[i][j][0] for j in range(one + 1)]))
            rowso.append(FenwickTree([dp[i][j][1] for j in range(one + 1)]))
        for j in range(one + 1):
            colsz.append(FenwickTree([dp[i][j][0] for i in range(zero + 1)]))
            colso.append(FenwickTree([dp[i][j][1] for i in range(zero + 1)]))
        for i in range(zero + 1):
            for j in range(one + 1):
                addz = colso[j].query(i) - colso[j].query(max(i - limit, 0))
                addo = rowsz[i].query(j) - rowsz[i].query(max(j - limit, 0))
                dp[i][j][0] += addz
                dp[i][j][0] %= M
                dp[i][j][1] += addo
                dp[i][j][1] %= M
                rowsz[i].update(j, addz)
                rowso[i].update(j, addo)
                colsz[j].update(i, addz)
                colso[j].update(i, addo)
        return (dp[zero][one][0] + dp[zero][one][1]) % M