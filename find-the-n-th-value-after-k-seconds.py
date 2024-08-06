class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        res = [1] * n
        M = 10 ** 9 + 7
        for _ in range(k):
            for i in range(1, n):
                res[i] += res[i - 1]
                res[i] %= M
        return res[-1]