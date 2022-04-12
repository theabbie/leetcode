class Solution:
    def countOrders(self, n: int) -> int:
        if n == 1:
            return 1
        val = self.countOrders(n - 1) * n * (2 * n - 1)
        return val % (10 ** 9 + 7)