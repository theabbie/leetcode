M = 10 ** 9 + 7
MAX = 1001
f = [1] * (MAX + 1)
rf = [1] * (MAX + 1)
for i in range(1, MAX + 1):
    f[i] = i * f[i - 1]
    f[i] %= M
rf[MAX] = pow(f[i], M - 2, M)
for i in range(MAX - 1, -1, -1):
    rf[i] = (i + 1) * rf[i + 1]
    rf[i] %= M

class Solution:
    def countOrders(self, n: int) -> int:
        if n == 1:
            return 1
        l = n - n % 2
        res = self.countOrders(l // 2) ** 2
        res *= f[2 * l] * rf[l] * rf[l]
        if n & 1:
            res *= f[2 * l + 2] * rf[2] * rf[2 * l]
        res %= M
        return res