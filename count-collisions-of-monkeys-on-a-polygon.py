class Solution:
    def monkeyMove(self, n: int) -> int:
        M = 10 ** 9 + 7
        return (M + pow(2, n, M) - 2) % M