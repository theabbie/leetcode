class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1 and k == 1:
            return 0
        prev = self.kthGrammar(n - 1, (k + 1) >> 1)
        if k & 1:
            return prev
        return 1 - prev