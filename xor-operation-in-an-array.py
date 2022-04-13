class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        op = start
        for i in range(1, n):
            op = op ^ (start + 2 * i)
        return op