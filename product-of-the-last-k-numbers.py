class ProductOfNumbers:
    def __init__(self):
        self.LOG = 20
        self.dp = [[1] * self.LOG]
        self.parent = [[0] * self.LOG]

    def add(self, num: int) -> None:
        i = len(self.dp)
        ndp = [num] + [1] * (self.LOG - 1)
        npar = [i - 1] + [0] * (self.LOG - 1)
        for j in range(1, self.LOG):
            npar[j] = self.parent[npar[j - 1]][j - 1]
            ndp[j] = ndp[j - 1] * self.dp[npar[j - 1]][j - 1]
        self.dp.append(ndp)
        self.parent.append(npar)

    def getProduct(self, k: int) -> int:
        pos, res, bit = len(self.dp) - 1, 1, 0
        while k:
            if k & 1:
                res *= self.dp[pos][bit]
                pos = self.parent[pos][bit]
            k //= 2
            bit += 1
        return res