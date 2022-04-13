class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n == 1:
            return [0, 1]
        prev = self.grayCode(n - 1)
        k = 1 << (n - 1)
        return prev + [prev[i] + k for i in range(k - 1, -1, -1)]