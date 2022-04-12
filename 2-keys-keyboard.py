class Solution:
    def minSteps(self, n: int, k = 1, clipboard = 0) -> int:
        if k == n:
            return 0
        if k > n:
            return float('inf')
        a = float('inf')
        if clipboard > 0:
            a = 1 + self.minSteps(n, k + clipboard, clipboard)
        b = 2 + self.minSteps(n, 2 * k, k)
        return min(a, b)