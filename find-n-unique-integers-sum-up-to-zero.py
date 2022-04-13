class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n == 1:
            return [0]
        if n == 2:
            return [-1, 1]
        prev = self.sumZero(n - 2)
        return [prev[0] - 1] + prev + [prev[-1] + 1]