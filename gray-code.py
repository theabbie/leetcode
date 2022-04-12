class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n == 1:
            return [0, 1]
        prev = self.grayCode(n - 1)
        return prev + [el + (1 << (n - 1)) for el in prev[::-1]]